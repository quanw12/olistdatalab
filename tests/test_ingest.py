import pytest

from olist_platform.ingest import ContractError, check_schema, ingest_all, ingest_table


def test_sample_ingests_cleanly(con, contract, landing, tmp_path):
    outcome = ingest_all(con, contract, landing, tmp_path / "lake", run_id="r1")
    assert outcome["orders"] == "loaded"
    assert outcome["geolocation"] == "absent"  # optional file
    assert con.execute("SELECT count(*) FROM bronze.orders").fetchone()[0] == 300
    assert (tmp_path / "lake" / "bronze" / "orders" / "orders.parquet").exists()


def test_rerun_with_same_files_is_skipped(con, contract, landing, tmp_path):
    ingest_all(con, contract, landing, tmp_path / "lake", run_id="r1")
    outcome = ingest_all(con, contract, landing, tmp_path / "lake", run_id="r2")
    assert set(outcome.values()) == {"skipped", "absent"}
    loads = con.execute("SELECT count(*) FROM audit.ingest_manifest WHERE table_name='orders'")
    assert loads.fetchone()[0] == 1


def test_lineage_columns_are_added(con, contract, landing, tmp_path):
    ingest_all(con, contract, landing, tmp_path / "lake", run_id="r1")
    row = con.execute("SELECT DISTINCT _source_file, _run_id FROM bronze.orders").fetchall()
    assert row == [("olist_orders_dataset.csv", "r1")]


def test_missing_column_is_schema_drift(contract):
    with pytest.raises(ContractError, match="missing columns"):
        check_schema(contract.tables["orders"], ["order_id", "customer_id"])


def test_extra_column_is_reported_not_fatal(contract):
    header = contract.tables["sellers"].columns + ["new_col"]
    assert check_schema(contract.tables["sellers"], header) == ["new_col"]


def _rewrite(path, transform):
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(transform(lines)) + "\n", encoding="utf-8")


def test_duplicate_key_blocks_publish_and_keeps_previous_bronze(con, contract, landing, tmp_path):
    lake = tmp_path / "lake"
    ingest_all(con, contract, landing, lake, run_id="good")
    path = landing / contract.tables["orders"].file
    _rewrite(path, lambda lines: lines + [lines[1]])  # duplicate the first order

    with pytest.raises(ContractError, match="primary_key_unique"):
        ingest_table(con, contract.tables["orders"], path, lake, "bad",
                     contract.timestamp_format)
    # Yesterday's good bronze table is still there, untouched.
    assert con.execute("SELECT DISTINCT _run_id FROM bronze.orders").fetchall() == [("good",)]
    failed = con.execute(
        "SELECT failed_rows FROM audit.quality_results WHERE run_id='bad' "
        "AND check_name LIKE 'primary_key_unique%'"
    ).fetchone()[0]
    assert failed == 1


def test_unknown_status_and_bad_timestamp_fail(con, contract, landing, tmp_path):
    path = landing / contract.tables["orders"].file

    def corrupt(lines):
        cells = lines[1].split(",")
        cells[2], cells[3] = "lost", "02/10/2017 10:56"
        return [lines[0], ",".join(cells)] + lines[2:]

    _rewrite(path, corrupt)
    with pytest.raises(ContractError) as err:
        ingest_table(con, contract.tables["orders"], path, tmp_path, "r",
                     contract.timestamp_format)
    assert "accepted_values(order_status)" in str(err.value)
    assert "parseable_timestamp(order_purchase_timestamp)" in str(err.value)


def test_messy_status_casing_is_a_warning_not_an_error(con, contract, landing, tmp_path):
    path = landing / contract.tables["orders"].file

    def mess(lines):
        cells = lines[1].split(",")
        cells[2] = " Delivered "
        return [lines[0], ",".join(cells)] + lines[2:]

    _rewrite(path, mess)
    status, results = ingest_table(con, contract.tables["orders"], path, tmp_path, "r",
                                   contract.timestamp_format)
    assert status == "loaded"
    warn = {r.check: r.failed_rows for r in results if r.severity == "warn"}
    assert warn["status_needs_normalizing"] >= 1


def test_missing_required_file_fails(con, contract, landing, tmp_path):
    (landing / contract.tables["sellers"].file).unlink()
    with pytest.raises(ContractError, match="required file not found"):
        ingest_all(con, contract, landing, tmp_path / "lake", run_id="r1")


def test_snapshot_revert_publishes_previously_seen_content(con, contract, landing, tmp_path):
    table = contract.tables["sellers"]
    path = landing / table.file
    original = path.read_bytes()
    ingest_table(con, table, path, tmp_path, "a", contract.timestamp_format)
    _rewrite(path, lambda lines: [lines[0]] + lines[1:-1])
    ingest_table(con, table, path, tmp_path, "b", contract.timestamp_format)
    path.write_bytes(original)
    status, _ = ingest_table(con, table, path, tmp_path, "a-again", contract.timestamp_format)
    assert status == "loaded"
    assert con.execute("SELECT DISTINCT _run_id FROM bronze.sellers").fetchall() == [("a-again",)]


@pytest.mark.parametrize("damage", ["missing", "stale"])
def test_rerun_repairs_parquet_without_reloading(con, contract, landing, tmp_path, damage):
    table = contract.tables["sellers"]
    path = landing / table.file
    ingest_table(con, table, path, tmp_path, "a", contract.timestamp_format)
    target = tmp_path / "bronze" / "sellers" / "sellers.parquet"
    if damage == "missing":
        target.unlink()
    else:
        target.write_bytes(b"interrupted or stale output")
    status, _ = ingest_table(con, table, path, tmp_path, "retry", contract.timestamp_format)
    assert status == "skipped"
    assert con.execute("SELECT count(*) FROM read_parquet(?)", [str(target)]).fetchone() == (
        con.execute("SELECT count(*) FROM bronze.sellers").fetchone()
    )
    assert con.execute("SELECT count(*) FROM audit.ingest_manifest").fetchone()[0] == 1
