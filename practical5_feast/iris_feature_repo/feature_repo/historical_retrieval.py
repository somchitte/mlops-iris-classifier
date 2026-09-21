from feast import FeatureStore
import pandas as pd


# Connect to Feast feature repository
store = FeatureStore(repo_path=".")


# Load the feature source data
df = pd.read_parquet("data/iris_features.parquet")


# Select first 5 samples
entity_df = df[
    [
        "sample_id",
        "event_timestamp",
    ]
].head(5)


print("Entity Data:")
print(entity_df)


# Retrieve historical features
historical_features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_measurements:sepal length (cm)",
        "iris_measurements:sepal width (cm)",
        "iris_measurements:petal length (cm)",
        "iris_measurements:petal width (cm)",
        "iris_engineered_features:sepal_area",
        "iris_engineered_features:petal_length_bin",
        "iris_engineered_features:petal_area",
        "iris_engineered_features:sepal_to_petal_length_ratio",
    ],
).to_df()


print("\nHistorical Feature Retrieval Result:")
print(historical_features)