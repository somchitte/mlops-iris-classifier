Iris Dataset DVC Pipeline

This project implements a modular DVC (Data Version Control) pipeline to collect, preprocess, feature-engineer, and validate the Iris dataset.

The pipeline consists of four stages:

Collect → Preprocess → Feature Engineering → Validate


DVC manages the dependencies between stages and automatically determines which stages need to be executed when data, code, or pipeline configuration changes.

Pipeline At A Glance
Stage	Purpose	Input	Output
Collect	Obtain the raw Iris dataset	Scikit-learn Iris dataset	data/raw/iris_raw.csv
Preprocess	Clean and prepare the raw data	data/raw/iris_raw.csv	data/processed/iris_preprocessed.csv
Feature Engineering	Create useful derived features	data/processed/iris_preprocessed.csv	data/processed/iris_features.csv
Validate	Check schema, nulls, and value ranges	data/processed/iris_features.csv	Validation result
Project Pipeline
Scikit-learn Iris Dataset
          │
          ▼
      ┌─────────┐
      │ Collect │
      └────┬────┘
           │
           │ data/raw/iris_raw.csv
           ▼
    ┌─────────────┐
    │ Preprocess  │
    └──────┬──────┘
           │
           │ data/processed/iris_preprocessed.csv
           ▼
 ┌─────────────────────┐
 │ Feature Engineering │
 └──────────┬──────────┘
            │
            │ data/processed/iris_features.csv
            ▼
      ┌──────────┐
      │ Validate │
      └────┬─────┘
           │
           ▼
    Validation Passed

Pipeline Stages
1. Collect
Purpose

The Collect stage obtains the Iris dataset using Scikit-learn and saves it as a raw CSV file.

Input

The Iris dataset provided by Scikit-learn.

Processing

The stage:

Loads the dataset using load_iris(as_frame=True).

Renames the target column to species.

Converts target values to:

setosa

versicolor

virginica

Adds a UTC collected_at timestamp.

Saves the dataset as a CSV file.

Output
data/raw/iris_raw.csv


The collected dataset contains 150 rows.

2. Preprocess
Purpose

The Preprocess stage cleans the raw dataset and prepares it for feature engineering.

Input
data/raw/iris_raw.csv

Processing

The stage:

Removes exact duplicate rows.

Converts numeric columns to numeric data types.

Handles missing numeric values using median imputation.

Removes rows with a missing species value.

Removes the collected_at column.

Output
data/processed/iris_preprocessed.csv

Current Result

One duplicate row was removed.

Raw rows:        150
Duplicates:       1
Processed rows:  149

3. Feature Engineering
Purpose

The Feature Engineering stage creates additional features from the preprocessed measurements.

Input
data/processed/iris_preprocessed.csv

Features Created
Feature	Definition
sepal_area	sepal length × sepal width
petal_area	petal length × petal width
sepal_to_petal_length_ratio	sepal length ÷ petal length
Petal length bin	Categorizes petal length as short, medium, or long
Output
data/processed/iris_features.csv


The resulting dataset contains 9 columns.

4. Validate
Purpose

The Validate stage checks whether the feature-engineered dataset satisfies the required schema and value constraints.

Input
data/processed/iris_features.csv

Validation Rules

The pipeline verifies that:

Required measurement columns are present.

The species column is present.

All engineered feature columns are present.

Species values are limited to:

setosa

versicolor

virginica

Numeric values are within the expected ranges.

Required data is valid before the pipeline completes.

Range Checks
Column	Minimum	Maximum
Sepal length	3.0	9.0
Sepal width	1.5	5.5
Petal length	0.5	8.0
Petal width	0.05	3.0

If validation fails, the pipeline exits with a non-zero status.

Output

The Validate stage does not create a new data file. Instead, it produces a validation result.

Current result:

Validation PASSED: 149 rows, 9 columns, all checks satisfied.

DVC Pipeline

The complete pipeline is defined in:

dvc.yaml


DVC tracks the dependencies and outputs for each stage.

The pipeline contains the following stages:

Order	Stage
1	Collect
2	Preprocess
3	Feature Engineering
4	Validate

The pipeline state and exact data dependencies are recorded in:

dvc.lock

Running the Pipeline

To reproduce the complete pipeline, run:

dvc repro


DVC checks whether any dependencies have changed.

If nothing has changed, DVC skips the stages that are already up to date.

A typical result is:

Stage collect didn't change, skipping
Stage preprocess didn't change, skipping
Stage features didn't change, skipping
Stage validate didn't change, skipping

Data and pipelines are up to date.


This prevents unnecessary processing.

DVC Remote Storage

The project uses a local DVC remote named:

myremote


The remote storage location is:

C:/Users/HP/dvc-remote-storage


To upload DVC-tracked data objects to the remote, run:

dvc push

Versioning and Reproducibility

DVC uses hashes to track data and pipeline dependencies.

The dvc.lock file stores the exact versions and hashes required to reproduce the pipeline.

This enables the project to:

Track changes to datasets.

Reproduce previous pipeline states.

Avoid unnecessary stage execution.

Maintain consistency between data and code.

Detect changes in pipeline dependencies.

Keep data versions synchronized with pipeline versions.

Data Flow

The complete automated flow is:

Raw Iris Dataset
       │
       ▼
    Collect
       │
       ▼
 iris_raw.csv
       │
       ▼
   Preprocess
       │
       ▼
iris_preprocessed.csv
       │
       ▼
Feature Engineering
       │
       ▼
 iris_features.csv
       │
       ▼
    Validate
       │
       ▼
Validation Passed

Current Pipeline Results
Metric	Result
Raw rows	150
Duplicate rows removed	1
Processed rows	149
Final rows	149
Final columns	9
Validation status	PASSED
Requirements

The project requires Python and the relevant data-processing and DVC dependencies.

Install DVC using:

pip install dvc


If the project contains a requirements.txt file, install the remaining dependencies with:

pip install -r requirements.txt

Useful DVC Commands
Reproduce the pipeline
dvc repro

Check pipeline status
dvc status

Push data to the DVC remote
dvc push

Pull data from the DVC remote
dvc pull

View the pipeline graph
dvc dag

Check configured DVC remotes
dvc remote list

Conclusion

This project demonstrates a modular and reproducible data-processing workflow using DVC and the Iris dataset.

The pipeline separates the workflow into four independent stages:

Collect
   ↓
Preprocess
   ↓
Feature Engineering
   ↓
Validate


DVC automatically manages stage dependencies and determines which stages need to run when source data, code, or pipeline dependencies change.

The current pipeline successfully produces a 149-row, 9-column feature-engineered dataset, and all validation checks pass successfully.

The project therefore provides a practical example of:

Data collection

Data preprocessing

Feature engineering

Automated data validation

Data version control

Pipeline dependency management

Reproducible data workflows