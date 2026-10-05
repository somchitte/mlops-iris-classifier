from feast import FeatureStore
from sklearn.cluster import KMeans
import pandas as pd


# Connect to Feast
store = FeatureStore(repo_path=".")


# Load sample IDs from the feature source
df = pd.read_parquet("data/iris_features.parquet")

entity_df = df[["sample_id", "event_timestamp"]]


# Retrieve the same features from Feast
features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_measurements:sepal length (cm)",
        "iris_measurements:sepal width (cm)",
        "iris_measurements:petal length (cm)",
        "iris_measurements:petal width (cm)",
        "iris_engineered_features:sepal_area",
        "iris_engineered_features:petal_area",
        "iris_engineered_features:sepal_to_petal_length_ratio",
    ],
).to_df()


# Select numerical features for clustering
X = features[
    [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "sepal_area",
        "petal_area",
        "sepal_to_petal_length_ratio",
    ]
]


# Perform clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10,
)

features["cluster"] = kmeans.fit_predict(X)


# Display results
print("Feature Reuse - Clustering Result:")
print(
    features[
        [
            "sample_id",
            "cluster",
        ]
    ].head(20)
)

print("\nTotal samples:", len(features))
print("Number of clusters:", features["cluster"].nunique())