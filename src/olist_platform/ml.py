"""Predict late deliveries from information known when the order is approved.

The data-engineering part matters more than the model:
- features come only from columns known at approval time (no leakage: delivery dates, review
  scores and the late flag itself are excluded),
- the split is by time (train on older orders, test on newer), like the model would be used,
- every run is tracked in MLflow (params, metrics, model) so results are reproducible.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import duckdb
import pandas as pd

from olist_platform.config import PROJECT_DIR

logger = logging.getLogger(__name__)

FEATURE_SQL = """
SELECT
    o.order_id,
    o.order_date,
    o.is_late,
    o.customer_state,
    s.state                                         AS seller_state,
    o.customer_state = s.state                      AS same_state,
    o.item_count,
    o.items_price,
    o.items_freight,
    o.items_freight / NULLIF(o.items_price, 0)      AS freight_ratio,
    o.seller_count,
    o.max_installments,
    o.payment_types LIKE '%boleto%'                 AS paid_boleto,
    date_diff('day', o.order_date, o.estimated_delivery_date) AS promised_days,
    isodow(o.order_date)                            AS purchase_dow,
    month(o.order_date)                             AS purchase_month,
    p.weight_g,
    p.volume_cm3
FROM marts.fct_orders o
LEFT JOIN marts.dim_sellers s ON s.seller_id = o.first_seller_id
LEFT JOIN (
    SELECT i.order_id, sum(d.weight_g) AS weight_g, sum(d.volume_cm3) AS volume_cm3
    FROM marts.fct_order_items i JOIN marts.dim_products d USING (product_id)
    GROUP BY i.order_id
) p ON p.order_id = o.order_id
WHERE o.order_status = 'delivered' AND o.is_late IS NOT NULL
"""

CATEGORICAL = ["customer_state", "seller_state"]
NUMERIC = ["item_count", "items_price", "items_freight", "freight_ratio", "seller_count",
           "max_installments", "promised_days", "purchase_dow", "purchase_month", "weight_g",
           "volume_cm3"]
BOOLEAN = ["same_state", "paid_boleto"]


def load_features(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    return con.execute(FEATURE_SQL).df()


def time_split(df: pd.DataFrame, test_fraction: float = 0.2) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Older orders train, newest test_fraction tests. Never a random split on time data."""
    df = df.sort_values("order_date")
    cut = int(len(df) * (1 - test_fraction))
    return df.iloc[:cut], df.iloc[cut:]


def build_model():
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder

    pre = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL),
        ("num", SimpleImputer(strategy="median"), NUMERIC + BOOLEAN),
    ])
    clf = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05,
                                         class_weight="balanced", random_state=0)
    return Pipeline([("pre", pre), ("clf", clf)])


def train(con: duckdb.DuckDBPyConnection, model_dir: Path) -> dict[str, float]:
    import joblib
    from sklearn.metrics import average_precision_score, roc_auc_score

    df = load_features(con)
    df[BOOLEAN] = df[BOOLEAN].astype(float)
    train_df, test_df = time_split(df)
    if train_df["is_late"].nunique() < 2 or test_df["is_late"].nunique() < 2:
        raise ValueError("need late and on-time orders in both train and test sets")

    model = build_model()
    features = CATEGORICAL + NUMERIC + BOOLEAN
    model.fit(train_df[features], train_df["is_late"].astype(int))
    scores = model.predict_proba(test_df[features])[:, 1]
    y_test = test_df["is_late"].astype(int)
    metrics = {
        "rows_train": float(len(train_df)),
        "rows_test": float(len(test_df)),
        "late_rate_test": float(y_test.mean()),
        "roc_auc": float(roc_auc_score(y_test, scores)),
        # Precision-recall is the honest metric when only a few orders are late.
        "average_precision": float(average_precision_score(y_test, scores)),
    }
    model_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_dir / "late_delivery.joblib")
    (model_dir / "late_delivery_metrics.json").write_text(json.dumps(metrics, indent=2))
    _log_mlflow(metrics, model_dir)
    logger.info("late-delivery model: %s", metrics)
    return metrics


def _log_mlflow(metrics: dict[str, float], model_dir: Path) -> None:
    try:
        import mlflow
    except ImportError:
        logger.info("mlflow not installed; metrics saved to %s only", model_dir)
        return
    # MLflow 3 needs a database backend; a local SQLite file is enough for one person.
    default_uri = f"sqlite:///{(PROJECT_DIR / 'mlflow.db').as_posix()}"
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI") or default_uri)
    mlflow.set_experiment("olist-late-delivery")
    with mlflow.start_run():
        mlflow.log_params({"model": "HistGradientBoostingClassifier", "split": "time 80/20",
                           "features": ",".join(CATEGORICAL + NUMERIC + BOOLEAN)})
        mlflow.log_metrics(metrics)
        mlflow.log_artifact(str(model_dir / "late_delivery.joblib"))
