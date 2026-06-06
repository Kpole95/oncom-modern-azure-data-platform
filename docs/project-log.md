# Project Log

## Phase 1 – Azure Setup

Created the main Azure resources:

* Resource group
* ADLS Gen2 storage account
* Databricks workspace
* Azure Data Factory
* Azure SQL databases
* Azure Key Vault
* Azure DevOps project

## Phase 2 – Secure Access Setup

Configured Key Vault-backed Databricks secrets and ADLS OAuth access. Verified that Databricks could access the storage container securely.

## Phase 3 – Source Ingestion

Implemented custom CDM/CSV ingestion for headerless source files. Source schemas were applied before writing Delta outputs.

## Phase 4 – Raw Layer

Built Raw ingestion for Purchase, Sales, HR, and Reference datasets.

## Phase 5 – Bronze Layer

Registered Raw Delta outputs as Bronze Databricks tables.

## Phase 6 – Silver Layer

Built Silver dimensions and facts for analytics and reporting. Applied deduplication, type casting, timestamp handling, key creation, and business calculations.

## Phase 7 – Power BI Reporting

Exported curated Silver tables and built Power BI report pages using star-schema relationships and DAX measures.

## Phase 8 – Data Quality SQL Layer

Created Azure SQL metadata tables, incremental mappings, result tables, stored procedure, and rule/failed-result views.

## Phase 9 – ADF Metadata Migration

Built Azure Data Factory pipeline to migrate changed Data Quality metadata from source database to dev database using watermark logic.

## Phase 10 – Databricks Data Quality Execution

Built Data Quality notebooks to read rule metadata, execute checks, write result rows, and capture bad records.

## Phase 11 – Operational Issue Tracking

Connected failed DQ results to Logic App / Azure DevOps bug creation flow for operational follow-up.

## Final Status

The project now demonstrates a complete Azure Data Engineering workflow from ingestion to reporting and Data Quality validation.

It is suitable for showcasing Azure Data Engineering, Databricks, PySpark, Delta Lake, Power BI, ADF, SQL metadata design, and DevOps practices.
