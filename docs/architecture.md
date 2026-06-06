# Architecture

## High-Level Architecture


Microsoft Dynamics-style CDM/CSV Export
        |
        v
Azure Data Lake Storage Gen2
        |
        v
Azure Databricks Raw Layer
        |
        v
Delta Lake Raw Storage
        |
        v
Azure Databricks Bronze Tables
        |
        v
Azure Databricks Silver Dimensions and Facts
        |
        v
Databricks Workflows
        |
        v
Power BI Reporting Model


## Data Quality Flow


Azure SQL DQ Metadata Source
        |
        v
Azure Data Factory Incremental Migration
        |
        v
Azure SQL DQ Dev Database
        |
        v
Databricks DQ Rule Execution
        |
        v
DQ Results + Bad Records
        |
        v
Failed Results View
        |
        v
Logic App / Azure DevOps Bug Tracking


## Layer Responsibilities

### Source Layer

The source layer contains Microsoft Dynamics-style CDM/CSV exports in ADLS Gen2. The data is stored as headerless CSV files with schema information available in CDM JSON metadata files.

### Raw Layer

The Raw layer reads source CSV files, applies schemas from CDM metadata, and writes the result as Delta Lake datasets.

### Bronze Layer

The Bronze layer registers Raw Delta outputs as Databricks tables. Bronze keeps the structure close to source while making data queryable and reusable.

### Silver Layer

The Silver layer creates analytics-ready dimensions and facts. It applies cleaning, type casting, deduplication, enrichment, joins, date keys, and business calculations.

### Reporting Layer

Power BI uses the curated Silver tables as its semantic source. The reporting model follows a star-schema structure with fact tables connected to dimensions.

### Data Quality Layer

The Data Quality layer stores metadata in Azure SQL, migrates rule metadata with ADF, executes rules in Databricks, captures bad records, stores execution results, and exposes failed rows for monitoring or bug creation.

## Key Design Choices

* Delta Lake is used for reliable lakehouse storage.
* Databricks is used for PySpark transformations and Data Quality execution.
* Azure SQL stores DQ rules and execution metadata.
* Azure Data Factory handles metadata movement and orchestration.
* Power BI consumes curated Silver-layer outputs.
* Azure DevOps tracks work items and DQ issues.
