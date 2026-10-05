# Feature Store Analysis

## 1. Introduction

A Feature Store is a centralized system used to manage, store, and serve machine learning features for different ML workflows.

In this practical, Feast was used to create a feature repository for the Iris dataset. The feature repository contains raw measurement features as well as engineered features.

The practical demonstrated both online and historical feature retrieval and showed how the same features can be reused for another machine learning task.

## 2. Feature Store Implementation

The following components were created using Feast:

- Entity: `sample`
- Data Source: `iris_features.parquet`
- Feature View: `iris_measurements`
- Feature View: `iris_engineered_features`
- Feature Service: `iris_feature_service`
- Online Store: SQLite
- Registry: SQLite

The feature repository provides a centralized location for defining and managing the features used by ML applications.

## 3. Online Feature Retrieval

Online feature retrieval was demonstrated using:

`sample_id = 1`

The retrieved features included:

- Sepal length
- Sepal width
- Petal length
- Petal width
- Sepal area
- Petal area
- Petal length bin
- Sepal-to-petal length ratio

The online retrieval successfully returned the feature values from the Feast online store.

This demonstrates how features can be retrieved for applications that require feature values during inference.

## 4. Historical / Offline Feature Retrieval

Historical feature retrieval was demonstrated using the event timestamps of the first five samples.

The retrieved data contained:

- `sample_id`
- `event_timestamp`
- Iris measurement features
- Engineered features

Point-in-time historical retrieval allows features to be obtained according to their corresponding event timestamps.

This is useful for creating training datasets while respecting the historical availability of feature values.

## 5. Feature Reusability

One of the important benefits demonstrated in this practical is feature reuse.

The features already defined in Feast were retrieved and reused for a K-Means clustering task.

The clustering experiment processed:

- 149 samples
- 3 clusters

The feature engineering logic did not need to be recreated separately for the clustering task.

This demonstrates how a Feature Store can provide reusable features for multiple machine learning workflows.

## 6. Reduction of Training-Serving Skew

Training-serving skew can occur when the feature engineering process used during model training is different from the process used during online inference.

A Feature Store helps reduce this problem by maintaining common feature definitions and making the same features available for both historical/offline retrieval and online retrieval.

In this practical, the same feature definitions were used for:

- Historical feature retrieval
- Online feature retrieval
- Feature reuse for clustering

Therefore, the feature definitions are centralized rather than being independently recreated for each workflow.

## 7. Centralized Feature Management and Governance

The Feast feature repository provides a centralized structure for managing features.

Feature definitions, feature views, entities, data sources, and feature services are maintained in the repository.

The `iris_feature_service` groups the required features together so that they can be retrieved consistently.

This centralized approach makes feature definitions easier to understand, maintain, and reuse across different ML workflows.

## 8. Benefits Observed

The practical demonstrated the following benefits of using a Feature Store:

1. Centralized feature definitions
2. Reusable features
3. Online feature retrieval
4. Historical/offline feature retrieval
5. Point-in-time feature retrieval
6. Reduced risk of training-serving skew
7. Easier feature management
8. Support for multiple machine learning workflows

## 9. Conclusion

This practical provided an introduction to Feature Stores using Feast.

A complete Iris feature repository was created with measurement and engineered features. The features were materialized into an online store and successfully retrieved for online inference.

Historical feature retrieval was also demonstrated using event timestamps. Finally, the same Feast-managed features were reused for K-Means clustering.

The practical shows how Feature Stores can provide centralized, reusable, and consistent feature management for machine learning workflows.