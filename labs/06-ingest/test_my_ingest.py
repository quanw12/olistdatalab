from pathlib import Path

import duckdb
import pytest
from my_ingest import (
    ContractError,
    check_header,
    ingest,
    load_candidate,
    load_contract,
    run_checks,
)

CONTRACT_FILE = Path(__file__).with_name("contract.yml")
HEADER = ("order_id,customer_id,order_status,order_purchase_timestamp,order_approved_at,"
          "order_delivered_carrier_date,order_delivered_customer_date,"
          "order_estimated_delivery_date\n")
ROW_1 = ("o1,c1,delivered,2017-10-02 10:56:33,2017-10-02 11:07:15,2017-10-04 19:55:00,"
         "2017-10-10 21:25:13,2017-10-18 00:00:00\n")
ROW_2 = ("o2,c2,shipped,2017-10-03 09:00:00,2017-10-03 10:00:00,2017-10-05 08:00:00,,"
         "2017-10-20 00:00:00\n")
ROW_LATE_NO_DATE = "o3,c3,delivered,2017-10-03 09:00:00,,,,2017-10-20 00:00:00\n"


@pytest.fixture
def contract():
    if not CONTRACT_FILE.exists():
        pytest.fail("write labs/06-ingest/contract.yml first (shape in my_ingest.py)")
    return load_contract(CONTRACT_FILE)


@pytest.fixture
def con():
    connection = duckdb.connect()
    yield connection
    connection.close()


@pytest.fixture
def csv(tmp_path):
    def write(*rows, header=HEADER, name="orders.csv"):
        path = tmp_path / name
        path.write_text(header + "".join(rows), encoding="utf-8")
        return path
    return write


def test_contract_shape(contract):
    assert contract["table"] == "orders"
    assert len(contract["columns"]) == 8
    assert contract["primary_key"] == ["order_id"]
    assert len(contract["accepted_values"]["order_status"]) == 8


def test_missing_column_is_rejected(contract, csv):
    with pytest.raises(ContractError, match="order_status"):
        check_header(csv(header="order_id,customer_id\n"), contract)


def test_extra_column_is_returned(contract, csv):
    path = csv(ROW_1.strip() + ",x\n", header=HEADER.strip() + ",new_col\n")
    assert check_header(path, contract) == ["new_col"]


def test_candidate_is_text_with_lineage(con, contract, csv):
    assert load_candidate(con, csv(ROW_1, ROW_2), contract) == 2
    types = dict(con.execute(
        "SELECT column_name, data_type FROM information_schema.columns "
        "WHERE table_name = 'orders__candidate'").fetchall())
    assert types["order_purchase_timestamp"] == "VARCHAR"
    assert {"_source_file", "_file_sha256", "_loaded_at"} <= set(types)


def checks_by_name(con, contract, path):
    load_candidate(con, path, contract)
    return {name: (sev, n) for name, sev, n in run_checks(con, "orders__candidate", contract)}


def test_clean_file_passes_every_error_check(con, contract, csv):
    results = checks_by_name(con, contract, csv(ROW_1, ROW_2))
    assert all(n == 0 for sev, n in results.values() if sev == "error")


def test_checks_count_bad_rows(con, contract, csv):
    bad_status = ROW_2.replace("o2", "o4").replace("shipped", "lost")
    bad_time = ROW_2.replace("o2", "o5").replace("2017-10-03 09:00:00", "03/10/2017 09:00")
    results = checks_by_name(con, contract, csv(ROW_1, ROW_1, bad_status, bad_time,
                                                ROW_LATE_NO_DATE))
    assert results["primary_key_unique"] == ("error", 1)
    assert results["accepted_values(order_status)"] == ("error", 1)
    assert results["parseable_timestamp(order_purchase_timestamp)"] == ("error", 1)
    assert results["delivered_without_delivery_date"] == ("warn", 1)
    assert results["not_null(customer_id)"] == ("error", 0)


def test_status_casing_is_not_an_error(con, contract, csv):
    messy = ROW_2.replace("shipped", " Shipped ")
    results = checks_by_name(con, contract, csv(messy))
    assert results["accepted_values(order_status)"] == ("error", 0)


def test_ingest_is_idempotent(con, contract, csv):
    path = csv(ROW_1, ROW_2)
    assert ingest(con, path, contract) == "loaded"
    assert ingest(con, path, contract) == "skipped"
    assert con.execute("SELECT count(*) FROM orders").fetchone()[0] == 2
    assert con.execute("SELECT count(*) FROM audit_manifest").fetchone()[0] == 1


def test_bad_file_keeps_previous_table(con, contract, csv, tmp_path):
    ingest(con, csv(ROW_1, ROW_2), contract)
    broken = csv(ROW_1, ROW_1, name="orders_v2.csv")
    with pytest.raises(ContractError, match="primary_key_unique"):
        ingest(con, broken, contract)
    ids = [r[0] for r in con.execute("SELECT order_id FROM orders ORDER BY 1").fetchall()]
    assert ids == ["o1", "o2"]
    assert con.execute("SELECT count(*) FROM audit_manifest").fetchone()[0] == 1


def test_changed_file_is_reloaded(con, contract, csv):
    ingest(con, csv(ROW_1), contract)
    assert ingest(con, csv(ROW_1, ROW_2), contract) == "loaded"
    assert con.execute("SELECT count(*) FROM orders").fetchone()[0] == 2
