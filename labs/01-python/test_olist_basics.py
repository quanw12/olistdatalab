import time
from datetime import UTC, datetime

import pytest
from olist_basics import (
    find_duplicates,
    normalize_status,
    parse_olist_time,
    read_orders,
    summarize_status,
)

HEADER = "order_id,customer_id,order_status,order_purchase_timestamp\n"


@pytest.mark.parametrize(("raw", "expected"), [
    (" Delivered ", "delivered"), ("shipped", "shipped"), ("CANCELED\t", "canceled"),
])
def test_normalize_status(raw, expected):
    assert normalize_status(raw) == expected


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_normalize_status_rejects_blank(raw):
    with pytest.raises(ValueError):
        normalize_status(raw)


def test_parse_time_converts_sao_paulo_to_utc():
    # October 2017: Sao Paulo was UTC-3 (summer time started later that month)
    assert parse_olist_time("2017-10-02 10:56:33") == datetime(2017, 10, 2, 13, 56, 33,
                                                               tzinfo=UTC)


def test_parse_time_handles_summer_time():
    # November 2017: Brazilian summer time, UTC-2
    assert parse_olist_time("2017-11-18 19:28:06") == datetime(2017, 11, 18, 21, 28, 6,
                                                               tzinfo=UTC)


@pytest.mark.parametrize("text", ["", "   "])
def test_parse_time_blank_is_none(text):
    assert parse_olist_time(text) is None


def test_parse_time_bad_text_names_the_value():
    with pytest.raises(ValueError, match="10/2/2017"):
        parse_olist_time("10/2/2017 10:56")


def test_find_duplicates():
    assert find_duplicates(["a", "b", "a", "c", "b", "a"]) == {"a", "b"}
    assert find_duplicates([]) == set()


def test_find_duplicates_is_fast():
    ids = [str(i) for i in range(200_000)] + ["42"]
    started = time.perf_counter()
    assert find_duplicates(ids) == {"42"}
    assert time.perf_counter() - started < 1.0


def test_read_orders_line_numbers_and_bom(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(HEADER + "o1,c1,delivered,2017-10-02 10:56:33\n"
                    "o2,c2,shipped,2017-10-03 09:00:00\n", encoding="utf-8-sig")
    rows = read_orders(path)
    assert [line for line, _ in rows] == [2, 3]
    assert rows[0][1]["order_id"] == "o1"


def test_read_orders_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="nope.csv"):
        read_orders(tmp_path / "nope.csv")


def test_summarize_status(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(HEADER + "o1,c1, Delivered ,x\no2,c2,delivered,x\no3,c3,shipped,x\n",
                    encoding="utf-8")
    assert summarize_status(read_orders(path)) == {"delivered": 2, "shipped": 1}
