# Databricks Setup

## Purpose

Azure Databricks is the main compute engine for the project. It is used for ingestion, transformation, Delta Lake table creation, workflow orchestration, and Data Quality execution.

## Workspace Setup

The Databricks workspace is configured with Unity Catalog enabled. Unity Catalog is used to organize schemas, tables, and volumes.

Main schemas:

bronze
silver
dataquality


## Notebook Organization

The Databricks notebooks are organized by processing layer:


notebooks/
├── raw/
├── bronze/
├── silver/
├── data_quality/
└── workflows/


## Shared Utilities

Reusable utilities handle:

* ADLS path constants
* secret retrieval
* OAuth configuration
* source reading
* Delta writes
* table registration
* SQL connectivity

## ADLS Access

Databricks reads from ADLS Gen2 using service principal OAuth credentials stored in a Key Vault-backed Databricks secret scope.

The project avoids hardcoded secrets and uses secure secret retrieval patterns.

## Custom Source Reader

The source files are headerless CSV files. A custom schema-driven reader is used to read CDM-style files.

The reader:

1. Reads CDM JSON metadata.
2. Builds Spark schemas.
3. Reads headerless CSV files.
4. Writes the output to Delta Lake.

## Data Quality Volumes

Data Quality outputs are written to Databricks volumes:


dqcheckresults
dqcheckbadrecords


These volumes store rule execution outputs and failed/bad records for investigation.

## Main Databricks Responsibilities

* Read raw source data
* Write Raw Delta datasets
* Register Bronze tables
* Build Silver dimensions and facts
* Run Data Quality rules
* Write results and bad records
* Support workflow orchestration
