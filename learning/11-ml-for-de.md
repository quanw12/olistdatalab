# 11 · ML for data engineers

**Time:** week 14 · **Stack:** scikit-learn, MLflow, pandas/NumPy, (PyTorch/TensorFlow/Keras: awareness)

## Why
Data engineers build the feature pipelines and training data that ML teams depend on. You need
to know what makes training data trustworthy: no leakage, correct time split, reproducibility.

## Learn
- Supervised learning basics: train/test, classification metrics (ROC-AUC, precision/recall,
  average precision for imbalanced data) — [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- Pipelines and `ColumnTransformer`; why preprocessing must be fit on train only
- Data leakage: features that are only known after the outcome
- Experiment tracking and model registry — [MLflow](https://mlflow.org/docs/latest/ml/tracking/)
- Feature stores (idea): the same feature definition for training and serving
- Deep learning frameworks (PyTorch, TensorFlow/Keras): know what they are for; one tutorial is enough at this stage

## Read in this repo
- `src/olist_platform/ml.py` — features in SQL, time split, MLflow logging.

## Build
1. `pip install -e ".[ml]"`, `olist ml-train` on the real data. Open `mlflow ui --backend-store-uri sqlite:///mlflow.db`.
2. Add a baseline (always predict the majority class; a logistic regression). The model must beat both.
3. Add a leakage test: a unit test that fails if any feature name is in a deny list
   (`delivered_at_utc`, `delivery_days`, `is_late`, review columns).
4. Move the feature query into a dbt model `ml_late_delivery_features` with tests; `ml.py` reads it.
5. Add batch scoring: `olist ml-score` writes `marts.order_late_risk` for orders not yet delivered.
6. Serve one prediction through the FastAPI app from module 04.

## Break it
- Add `delivery_days` as a feature. What happens to ROC-AUC, and why is the model now useless?
- Use a random split instead of the time split; compare metrics.

## Interview questions
- What is data leakage? Give an example from this project.
- Why does the train/test split follow time here?
- What does a data engineer own in an ML system?

## Done when
- [ ] Baselines, leakage test, dbt feature model and batch scoring merged
- [ ] Metrics on real data recorded in the README
