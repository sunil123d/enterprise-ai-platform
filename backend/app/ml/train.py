from pathlib import Path

import joblib
from xgboost import XGBClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report
)
from sklearn.model_selection import train_test_split

from app.ml.preprocess import load_and_preprocess_data


DATASET = Path("app/ml/datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv")
MODEL_DIR = Path("app/ml/models")

MODEL_DIR.mkdir(parents=True, exist_ok=True)


# Load dataset
X, y = load_and_preprocess_data(DATASET)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        random_state=42,
        eval_metric="logloss"
    )
}


best_model = None
best_auc = 0


for name, model in models.items():

    print("=" * 60)
    print(name)
    print("=" * 60)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, predictions)

    auc = roc_auc_score(y_test, probabilities)

    print(f"\nAccuracy : {accuracy:.4f}")
    print(f"ROC AUC  : {auc:.4f}")

    print("\nClassification Report\n")
    print(classification_report(y_test, predictions))

    if auc > best_auc:
        best_auc = auc
        best_model = model


joblib.dump(
    best_model,
    MODEL_DIR / "best_model.pkl"
)

print("\n")
print("=" * 60)
print("Best model saved successfully!")
print(f"Best ROC-AUC : {best_auc:.4f}")
print("=" * 60)