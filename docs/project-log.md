# Project Log

## Phase 1 - Azure Setup

Created the main Azure resources:

- Resource group (`rg-oncom-dev-001`)
- ADLS Gen2 storage account
- Databricks workspace
- Azure Data Factory
- Azure SQL databases
- Azure Key Vault
- Azure DevOps project

## Phase 2 - Secure Access Setup

Configured Key Vault-backed Databricks secrets and ADLS OAuth access. Verified that Databricks could read from the storage container securely without hardcoded credentials.

## Phase 3 - Source Ingestion

Implemented custom CDM/CSV ingestion for headerless source files. Schemas were read from CDM JSON metadata and applied before writing Delta outputs.

## Phase 4 - Raw Layer

Built Raw ingestion notebooks for Purchase, Sales, HR, and Reference datasets.

## Phase 5 - Bronze Layer

Registered Raw Delta outputs as Bronze tables in Unity Catalog.

## Phase 6 - Silver Layer

Built Silver dimension and fact notebooks for analytics and reporting. Applied deduplication, type casting, timestamp normalisation, surrogate key generation, and business calculations.

## Phase 7 - Power BI Reporting

Connected curated Silver tables to Power BI and built report pages using star-schema relationships and DAX measures.

## Phase 8 - Data Quality SQL Layer

Created Azure SQL metadata tables, incremental watermark mappings, result tables, stored procedure, and rule/failed-result views.

## Phase 9 - ADF Metadata Migration

Built an Azure Data Factory pipeline to migrate changed Data Quality metadata from the source database to the dev database using watermark-based incremental logic.

## Phase 10 - Databricks Data Quality Execution

Built Data Quality notebooks to read rule metadata from Azure SQL, execute checks against lakehouse tables, write result rows, and capture bad records to Databricks volumes.

## Phase 11 - Operational Issue Tracking

Connected failed DQ results to a Logic App / Azure DevOps bug creation flow for operational follow-up and issue management.

---

## Final Status

The project demonstrates a complete Azure Data Engineering workflow from ingestion to reporting and Data Quality validation. It covers Azure infrastructure, secure access patterns, lakehouse design, PySpark transformations, orchestration, Power BI reporting, SQL metadata design, and DevOps practices.
