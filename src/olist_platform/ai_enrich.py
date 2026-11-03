"""Label Portuguese review comments with an LLM: topic + sentiment, as structured data.

This is the data-engineering side of AI, not prompt tinkering:
- providers are swappable (keyword baseline, local Ollama, Anthropic API) behind one function,
- every answer is validated against a fixed schema; anything else is stored as 'unparsed',
- results are cached by review, input hash, prompt version, provider and model, so
  re-runs only pay for new reviews and a prompt change is a new, comparable version,
- quality is measured, not assumed: sentiment is compared with the customer's own 1-5 score.
"""

from __future__ import annotations

import json
import logging
import re
import unicodedata
from collections.abc import Callable
from datetime import UTC, datetime

import duckdb
import requests

from olist_platform.config import Settings

logger = logging.getLogger(__name__)

PROMPT_VERSION = "v1"
TOPICS = ["delivery", "product_quality", "wrong_or_missing_item", "seller_service", "price",
          "praise", "other"]
SENTIMENTS = ["positive", "neutral", "negative"]

PROMPT = """You label customer reviews from a Brazilian e-commerce marketplace.
The review is in Portuguese. Answer with JSON only, no other text:
{{"topic": one of {topics}, "sentiment": one of {sentiments}}}

Review: {text}"""

KEYWORDS = {
    "wrong_or_missing_item": ["não recebi", "nao recebi", "errado", "diferente", "faltou",
                              "faltando", "outro produto"],
    "delivery": ["entrega", "atras", "prazo", "chegou", "demor", "correio"],
    "product_quality": ["quebrad", "defeito", "qualidade", "estragad", "amassad"],
    "seller_service": ["vendedor", "resposta", "atendimento", "loja"],
    "price": ["preço", "preco", "caro", "barato", "dinheiro de volta", "reembolso"],
    "praise": ["excelente", "ótim", "otim", "recomendo", "perfeito", "adorei", "muito bom"],
}
NEGATIVE = ["não", "nao", "atras", "quebrad", "errado", "defeito", "demor", "péssim", "pessim",
            "dinheiro de volta", "diferente", "sem resposta"]
POSITIVE = ["excelente", "ótim", "otim", "recomendo", "perfeito", "adorei", "bom", "gostei",
            "antes do prazo", "dentro do prazo"]


def _fold(text: str) -> str:
    return unicodedata.normalize("NFC", text.lower())


def keyword_label(text: str) -> dict:
    """Deterministic baseline. Free, fast, used in CI; the bar an LLM has to beat."""
    t = _fold(text)
    topic = next((name for name, words in KEYWORDS.items() if any(w in t for w in words)),
                 "other")
    neg = sum(w in t for w in NEGATIVE)
    pos = sum(w in t for w in POSITIVE)
    sentiment = "negative" if neg > pos else "positive" if pos > neg else "neutral"
    return {"topic": topic, "sentiment": sentiment}


def parse_label(answer: str) -> dict | None:
    """Pull the first JSON object out of a model answer and check it against the schema."""
    match = re.search(r"\{.*?\}", answer, flags=re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    if data.get("topic") not in TOPICS or data.get("sentiment") not in SENTIMENTS:
        return None
    return {"topic": data["topic"], "sentiment": data["sentiment"]}


def _prompt(text: str) -> str:
    return PROMPT.format(topics=TOPICS, sentiments=SENTIMENTS, text=text[:1000])


def ollama_labeler(settings: Settings) -> Callable[[str], str]:
    def ask(text: str) -> str:
        response = requests.post(
            f"{settings.ollama_url}/api/chat",
            json={"model": settings.ollama_model, "stream": False, "format": "json",
                  "options": {"temperature": 0},
                  "messages": [{"role": "user", "content": _prompt(text)}]},
            timeout=120,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    return ask


def anthropic_labeler(settings: Settings) -> Callable[[str], str]:
    import anthropic  # optional dependency: pip install -e ".[ai]"

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

    def ask(text: str) -> str:
        message = client.messages.create(
            model=settings.anthropic_model, max_tokens=100, temperature=0,
            messages=[{"role": "user", "content": _prompt(text)}],
        )
        return message.content[0].text
    return ask


def ensure_table(con: duckdb.DuckDBPyConnection) -> None:
    con.execute("CREATE SCHEMA IF NOT EXISTS ai")
    legacy = con.execute(
        "SELECT count(*) FROM information_schema.columns "
        "WHERE table_schema='ai' AND table_name='review_labels'"
    ).fetchone()[0]
    has_hash = con.execute(
        "SELECT count(*) FROM information_schema.columns "
        "WHERE table_schema='ai' AND table_name='review_labels' "
        "AND column_name='input_sha256'"
    ).fetchone()[0]
    if legacy and not has_hash:
        # Preserve historical labels but never reuse an entry whose input is unknown.
        con.execute("BEGIN TRANSACTION")
        try:
            con.execute("ALTER TABLE ai.review_labels RENAME TO review_labels_legacy")
            _create_label_table(con)
            con.execute(
                "INSERT INTO ai.review_labels "
                "SELECT *, '' AS input_sha256 FROM ai.review_labels_legacy"
            )
            con.execute("DROP TABLE ai.review_labels_legacy")
            con.execute("COMMIT")
        except Exception:
            con.execute("ROLLBACK")
            raise
    else:
        _create_label_table(con)


def _create_label_table(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS ai.review_labels (
            review_id VARCHAR, order_id VARCHAR, prompt_version VARCHAR, provider VARCHAR,
            model VARCHAR, topic VARCHAR, sentiment VARCHAR, labeled_at TIMESTAMPTZ,
            input_sha256 VARCHAR,
            PRIMARY KEY (review_id, order_id, prompt_version, provider, model, input_sha256)
        )
        """
    )


def pending_reviews(con: duckdb.DuckDBPyConnection, provider: str, limit: int,
                    model: str) -> list[tuple]:
    return con.execute(
        """
        SELECT r.review_id, r.order_id, r.comment_message, sha256(r.comment_message)
        FROM staging.stg_order_reviews r
        WHERE r.comment_message IS NOT NULL
          AND NOT EXISTS (
              SELECT 1 FROM ai.review_labels l
              WHERE l.review_id = r.review_id AND l.order_id = r.order_id
                AND l.prompt_version = ? AND l.provider = ? AND l.model = ?
                AND l.input_sha256 = sha256(r.comment_message))
        ORDER BY r.review_id
        LIMIT ?
        """,
        [PROMPT_VERSION, provider, model, limit],
    ).fetchall()


def label_reviews(con: duckdb.DuckDBPyConnection, settings: Settings, provider: str,
                  limit: int = 200) -> int:
    ensure_table(con)
    if provider == "keyword":
        model = "rules"
        label = keyword_label
    else:
        ask = (ollama_labeler(settings) if provider == "ollama"
               else anthropic_labeler(settings) if provider == "anthropic" else None)
        if ask is None:
            raise ValueError(f"unknown provider {provider!r}")
        model = settings.ollama_model if provider == "ollama" else settings.anthropic_model

        def label(text: str) -> dict:
            for _ in range(2):  # one retry for an answer that breaks the schema
                parsed = parse_label(ask(text))
                if parsed:
                    return parsed
            return {"topic": "unparsed", "sentiment": "unparsed"}

    rows = pending_reviews(con, provider, limit, model)
    for review_id, order_id, text, input_sha256 in rows:
        result = label(text)
        con.execute(
            "INSERT INTO ai.review_labels VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [review_id, order_id, PROMPT_VERSION, provider, model, result["topic"],
             result["sentiment"], datetime.now(UTC), input_sha256],
        )
    logger.info("%s labeled %d new reviews", provider, len(rows))
    return len(rows)


def evaluate(con: duckdb.DuckDBPyConnection) -> list[tuple]:
    """Sentiment agreement with the review score (1-2 negative, 3 neutral, 4-5 positive)."""
    ensure_table(con)
    return con.execute(
        """
        SELECT l.provider, l.prompt_version, l.model, count(*) AS labeled,
               round(avg((l.sentiment = CASE WHEN r.review_score <= 2 THEN 'negative'
                                              WHEN r.review_score = 3 THEN 'neutral'
                                              ELSE 'positive' END)::INT), 3) AS agreement,
               round(avg((l.topic = 'unparsed')::INT), 3) AS unparsed_rate
        FROM ai.review_labels l
        JOIN staging.stg_order_reviews r USING (review_id, order_id)
        WHERE l.input_sha256 = sha256(r.comment_message)
        GROUP BY ALL ORDER BY ALL
        """
    ).fetchall()
