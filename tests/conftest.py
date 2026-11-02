from pathlib import Path

import duckdb
import pytest

from olist_platform.contracts import load_contract
from olist_platform.sample import generate


@pytest.fixture
def contract():
    return load_contract()


@pytest.fixture
def con():
    connection = duckdb.connect()
    connection.execute("CREATE SCHEMA bronze")
    connection.execute("CREATE SCHEMA audit")
    yield connection
    connection.close()


@pytest.fixture
def landing(tmp_path) -> Path:
    path = tmp_path / "landing" / "olist"
    generate(path, n_orders=300, seed=7)
    return path
