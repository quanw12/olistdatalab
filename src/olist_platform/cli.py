"""Command line entry point: `olist <command>` (or `python -m olist_platform <command>`).

Every command exits with code 1 on failure so a scheduler (Airflow, cron, CI) sees it.
"""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import UTC, datetime

from olist_platform import config
from olist_platform.runlog import connect, new_run_id, record_run, setup_logging

logger = logging.getLogger("olist")


def cmd_sample(args, settings) -> None:
    from olist_platform.sample import generate

    counts = generate(settings.landing_dir, n_orders=args.orders, seed=args.seed)
    logger.info("sample written to %s: %s", settings.landing_dir, counts)


def cmd_ingest(args, settings, run_id) -> None:
    from olist_platform.contracts import load_contract
    from olist_platform.ingest import ingest_all

    with connect(settings.duckdb_path) as con:
        started = datetime.now(UTC)
        outcome = ingest_all(con, load_contract(), settings.landing_dir, settings.lake_dir,
                             run_id, force=args.force)
        record_run(con, run_id, "ingest", "success", started, str(outcome))


def cmd_fx(args, settings, run_id) -> None:
    from olist_platform.fx import load_fx

    with connect(settings.duckdb_path) as con:
        started = datetime.now(UTC)
        n = load_fx(con, settings.landing_dir, run_id, offline=args.offline)
        record_run(con, run_id, "fx", "success", started, f"{n} rates")


def cmd_transform(args, settings, run_id) -> None:
    from olist_platform.transform import export_gold, run_dbt

    # dbt opens the DuckDB file itself; no connection may be open here meanwhile.
    run_dbt(settings.duckdb_path, "build", full_refresh=args.full_refresh)
    with connect(settings.duckdb_path) as con:
        started = datetime.now(UTC)
        counts = export_gold(con, settings.lake_dir)
        record_run(con, run_id, "transform", "success", started, str(counts))


def cmd_run(args, settings, run_id) -> None:
    """The daily batch: ingest -> fx -> dbt build -> gold Parquet."""
    cmd_ingest(args, settings, run_id)
    cmd_fx(args, settings, run_id)
    cmd_transform(args, settings, run_id)


def cmd_serve(args, settings, run_id) -> None:
    from olist_platform.serve import publish_to_postgres

    with connect(settings.duckdb_path) as con:
        publish_to_postgres(con, settings.postgres_dsn)


def cmd_ml_train(args, settings, run_id) -> None:
    from olist_platform.ml import train

    with connect(settings.duckdb_path) as con:
        train(con, config.PROJECT_DIR / "models")


def cmd_ai_label(args, settings, run_id) -> None:
    from olist_platform.ai_enrich import label_reviews

    with connect(settings.duckdb_path) as con:
        label_reviews(con, settings, args.provider or settings.llm_provider, limit=args.limit)


def cmd_ai_eval(args, settings, run_id) -> None:
    from olist_platform.ai_enrich import evaluate

    with connect(settings.duckdb_path) as con:
        for provider, version, model, labeled, agreement, unparsed in evaluate(con):
            print(f"{provider:<10} {version:<4} model={model} labeled={labeled:<6} "
                  f"sentiment_vs_score={agreement}  unparsed={unparsed}")


def cmd_stream_produce(args, settings, run_id) -> None:
    from olist_platform.streaming import produce

    produce(settings.kafka_bootstrap, settings.kafka_topic, settings.duckdb_path,
            limit=args.limit, rate_per_sec=args.rate)


def cmd_stream_consume(args, settings, run_id) -> None:
    from olist_platform.streaming import consume

    consume(settings.kafka_bootstrap, settings.kafka_topic,
            settings.duckdb_path.with_name("stream.duckdb"), idle_timeout_s=args.idle)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="olist", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("sample", help="generate synthetic Olist-shaped CSVs into landing/")
    p.add_argument("--orders", type=int, default=2000)
    p.add_argument("--seed", type=int, default=42)
    p.set_defaults(func=cmd_sample, needs_run=False)

    p = sub.add_parser("ingest", help="landing CSV -> contract checks -> bronze")
    p.add_argument("--force", action="store_true", help="reload files already loaded")
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("fx", help="BRL exchange rates -> bronze.fx_rates")
    p.add_argument("--offline", action="store_true", help="deterministic rates, no network")
    p.set_defaults(func=cmd_fx)

    p = sub.add_parser("transform", help="dbt build + export gold Parquet")
    p.add_argument("--full-refresh", action="store_true")
    p.set_defaults(func=cmd_transform)

    p = sub.add_parser("run", help="ingest + fx + transform")
    p.add_argument("--force", action="store_true")
    p.add_argument("--offline", action="store_true")
    p.add_argument("--full-refresh", action="store_true")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("serve", help="publish gold marts to PostgreSQL")
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("ml-train", help="train the late-delivery model (MLflow tracked)")
    p.set_defaults(func=cmd_ml_train)

    p = sub.add_parser("ai-label", help="label review comments with an LLM provider")
    p.add_argument("--provider", choices=["keyword", "ollama", "anthropic"])
    p.add_argument("--limit", type=int, default=200)
    p.set_defaults(func=cmd_ai_label)

    p = sub.add_parser("ai-eval", help="compare LLM sentiment with review scores")
    p.set_defaults(func=cmd_ai_eval)

    p = sub.add_parser("stream-produce", help="replay order lifecycles to Kafka")
    p.add_argument("--limit", type=int, default=500, help="orders to replay (0 = all)")
    p.add_argument("--rate", type=float, default=200.0, help="events per second (0 = max)")
    p.set_defaults(func=cmd_stream_produce)

    p = sub.add_parser("stream-consume", help="consume order events into stream.duckdb")
    p.add_argument("--idle", type=float, default=10.0, help="stop after N idle seconds")
    p.set_defaults(func=cmd_stream_consume)
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    settings = config.get_settings()
    setup_logging(settings.log_dir, args.command)
    try:
        if getattr(args, "needs_run", True):
            run_id = new_run_id()
            logger.info("%s started, run_id=%s", args.command, run_id)
            args.func(args, settings, run_id)
        else:
            args.func(args, settings)
    except Exception:
        logger.exception("%s failed", args.command)
        sys.exit(1)
    logger.info("%s finished", args.command)


if __name__ == "__main__":
    main()
