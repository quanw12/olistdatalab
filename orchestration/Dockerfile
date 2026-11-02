# Airflow image with the pipeline's dependencies. The project itself is mounted at /opt/olist
# (see docker-compose.yml), so code changes need no rebuild; dependency changes do.
FROM apache/airflow:3.1.0-python3.12

RUN pip install --no-cache-dir \
    "duckdb>=1.1" "pandas>=2.2" "pyarrow>=16" "requests>=2.32" "python-dotenv>=1.0" \
    "pyyaml>=6.0" tzdata "dbt-core>=1.10" "dbt-duckdb>=1.9" "scikit-learn>=1.5" joblib

ENV PYTHONPATH=/opt/olist/src
