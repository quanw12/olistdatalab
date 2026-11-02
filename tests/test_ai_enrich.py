import pytest

from olist_platform.ai_enrich import keyword_label, parse_label


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
