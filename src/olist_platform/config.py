"""Paths and settings. Everything comes from environment variables with local defaults."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_DIR / ".env")

# Olist timestamps carry no zone. The marketplace is Brazilian, so they are Sao Paulo local
# time. A zone name (not a fixed -03:00) is required: Brazil had summer time until 2019.
SOURCE_TIMEZONE = "America/Sao_Paulo"


def _path(env: str, default: str) -> Path:
    value = Path(os.getenv(env, default))
    return value if value.is_absolute() else PROJECT_DIR / value


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    duckdb_path: Path
    postgres_dsn: str
    kafka_bootstrap: str
    kafka_topic: str
    llm_provider: str
    ollama_url: str
    ollama_model: str
    anthropic_model: str

    @property
    def landing_dir(self) -> Path:
        """Source files exactly as received (Kaggle CSVs or the generated sample)."""
        return self.data_dir / "landing" / "olist"

    @property
    def lake_dir(self) -> Path:
        """Parquet files, partitioned by layer: bronze/ and gold/."""
        return self.data_dir / "lake"

    @property
    def log_dir(self) -> Path:
        return PROJECT_DIR / "logs"


def get_settings() -> Settings:
    return Settings(
        data_dir=_path("OLIST_DATA_DIR", "data"),
        duckdb_path=_path("DUCKDB_PATH", "data/warehouse/olist.duckdb"),
        postgres_dsn=os.getenv("POSTGRES_DSN", "postgresql://olist:olist@localhost:5432/olist"),
        kafka_bootstrap=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
        kafka_topic=os.getenv("KAFKA_TOPIC_ORDERS", "olist.orders.v1"),
        llm_provider=os.getenv("LLM_PROVIDER", "keyword"),
        ollama_url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
        ollama_model=os.getenv("OLLAMA_MODEL", "qwen2.5:3b"),
        anthropic_model=os.getenv("ANTHROPIC_MODEL", "claude-haiku-5-5"),
    )
