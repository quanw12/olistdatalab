"""Load the YAML source contracts shipped with the package."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

CONTRACT_FILE = Path(__file__).with_name("olist.yml")


@dataclass(frozen=True)
class TableContract:
    name: str
    file: str
    columns: list[str]
    grain: str = ""
    required: bool = True
    primary_key: list[str] = field(default_factory=list)
    not_null: list[str] = field(default_factory=list)
    accepted_values: dict[str, list[str]] = field(default_factory=dict)
    timestamps: list[str] = field(default_factory=list)
    numeric: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Contract:
    timestamp_format: str
    tables: dict[str, TableContract]


def load_contract(path: Path = CONTRACT_FILE) -> Contract:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    tables = {
        name: TableContract(
            name=name,
            accepted_values={k: [str(v) for v in vals]
                             for k, vals in spec.pop("accepted_values", {}).items()},
            **spec,
        )
        for name, spec in raw["tables"].items()
    }
    return Contract(timestamp_format=raw["timestamp_format"], tables=tables)
