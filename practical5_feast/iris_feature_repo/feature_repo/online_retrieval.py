from feast import FeatureStore


# Connect to Feast feature repository
store = FeatureStore(repo_path=".")


# Retrieve features for sample_id = 1
result = store.get_online_features(
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
    entity_rows=[
        {"sample_id": 1}
    ],
).to_dict()


print("Online Feature Retrieval Result:")

for key, value in result.items():
    print(f"{key}: {value}")