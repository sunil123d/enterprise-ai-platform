import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess_data(filepath):

    # ---------------------------------------
    # Load Dataset
    # ---------------------------------------

    df = pd.read_csv(filepath)

    print("\nOriginal Shape:", df.shape)

    # ---------------------------------------
    # Remove Customer ID
    # ---------------------------------------

    df.drop("customerID", axis=1, inplace=True)

    # ---------------------------------------
    # Convert TotalCharges to numeric
    # ---------------------------------------

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # ---------------------------------------
    # Fill Missing Values
    # ---------------------------------------

    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

    # ---------------------------------------
    # Encode Categorical Columns
    # ---------------------------------------

    print("\n==============================")
    print("Label Encoder Mappings")
    print("==============================\n")

    for column in df.columns:

        if df[column].dtype == "object":

            encoder = LabelEncoder()

            df[column] = encoder.fit_transform(df[column])

            print(f"{column}")

            mapping = dict(
                zip(
                    encoder.classes_,
                    encoder.transform(encoder.classes_)
                )
            )

            for key, value in mapping.items():
                print(f"   {key} --> {value}")

            print("--------------------------------")

    # ---------------------------------------
    # Dataset Info
    # ---------------------------------------

    print("\nProcessed Shape:", df.shape)

    # ---------------------------------------
    # Features and Target
    # ---------------------------------------

    X = df.drop("Churn", axis=1)

    y = df["Churn"]

    return X, y