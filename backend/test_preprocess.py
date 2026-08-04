from app.ml.preprocess import load_and_preprocess_data

X, y = load_and_preprocess_data(
    "app/ml/datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print()

print("Features Shape:", X.shape)

print("Target Shape:", y.shape)

print()

print(X.head())

print()

print(y.head())