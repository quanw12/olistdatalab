import pytest

from olist_platform.ai_enrich import (
    ensure_table,
    evaluate,
    keyword_label,
    label_reviews,
    parse_label,
    pending_reviews,
)
from olist_platform.config import get_settings


@pytest.mark.parametrize(("text", "topic", "sentiment"), [
    ("Não recebi o produto", "wrong_or_missing_item", "negative"),
    ("Entrega atrasada e sem resposta do vendedor", "delivery", "negative"),
    ("Produto excelente, chegou antes do prazo", "delivery", "positive"),
    ("Veio quebrado", "product_quality", "negative"),
])
def test_keyword_baseline(text, topic, sentiment):
    assert keyword_label(text) == {"topic": topic, "sentiment": sentiment}


def test_parse_label_accepts_json_wrapped_in_text():
    answer = 'Sure! {"topic": "delivery", "sentiment": "negative"} Hope this helps.'
    assert parse_label(answer) == {"topic": "delivery", "sentiment": "negative"}


@pytest.mark.parametrize("answer", [
    "no json here",
    '{"topic": "shipping", "sentiment": "negative"}',  # topic not in the schema
    '{"topic": "delivery", "sentiment": "angry"}',
    '{"topic": "delivery", "sentiment": ',
])
def test_parse_label_rejects_off_schema_answers(answer):
    assert parse_label(answer) is None


@pytest.fixture
def reviews(con):
    con.execute("CREATE SCHEMA staging")
    con.execute("CREATE TABLE staging.stg_order_reviews "
                "(review_id VARCHAR, order_id VARCHAR, comment_message VARCHAR, review_score INT)")
    con.execute("INSERT INTO staging.stg_order_reviews "
                "VALUES ('r1', 'o1', 'Entrega atrasada', 1)")
    return con


def test_cache_reuses_same_input_but_relabels_changed_text(reviews):
    settings = get_settings()
    assert label_reviews(reviews, settings, "keyword") == 1
    assert label_reviews(reviews, settings, "keyword") == 0
    reviews.execute("UPDATE staging.stg_order_reviews "
                    "SET comment_message='Produto excelente', review_score=5")
    assert label_reviews(reviews, settings, "keyword") == 1
    assert reviews.execute("SELECT count(*) FROM ai.review_labels").fetchone()[0] == 2
    # Historical input remains stored but is not scored against today's review.
    assert evaluate(reviews) == [("keyword", "v1", "rules", 1, 1.0, 0.0)]


def test_cache_distinguishes_models(reviews):
    label_reviews(reviews, get_settings(), "keyword")
    assert pending_reviews(reviews, "keyword", 10, "rules") == []
    assert len(pending_reviews(reviews, "keyword", 10, "rules-v2")) == 1


def test_legacy_cache_migration_preserves_labels_without_reusing_unknown_input(reviews):
    reviews.execute("CREATE SCHEMA ai")
    reviews.execute("""
        CREATE TABLE ai.review_labels (
            review_id VARCHAR, order_id VARCHAR, prompt_version VARCHAR, provider VARCHAR,
            model VARCHAR, topic VARCHAR, sentiment VARCHAR, labeled_at TIMESTAMPTZ,
            PRIMARY KEY (review_id, order_id, prompt_version, provider)
        )
    """)
    reviews.execute("INSERT INTO ai.review_labels VALUES "
                    "('r1','o1','v1','keyword','rules','delivery','negative',current_timestamp)")
    ensure_table(reviews)
    ensure_table(reviews)  # migration is safe to revisit
    assert reviews.execute("SELECT input_sha256 FROM ai.review_labels").fetchall() == [("",)]
    assert label_reviews(reviews, get_settings(), "keyword") == 1
    assert reviews.execute("SELECT count(*) FROM ai.review_labels").fetchone()[0] == 2
