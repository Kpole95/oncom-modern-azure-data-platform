# Databricks Setup

## Purpose

Azure Databricks is the main compute engine for the project. It handles ingestion, transformation, Delta Lake table creation, workflow orchestration, and Data Quality execution.

---

## Workspace Setup

The Databricks workspace is configured with Unity Catalog enabled. Unity Catalog organises schemas, tables, and volumes.

Main schemas:

```
bronze
silver
dataquality
```

---

## Notebook Organisation

Notebooks are structured by processing layer:

```
notebooks/
├── raw/
├── bronze/
├── silver/
├── data_quality/
└── workflows/
```

---

## Shared Utilities

Reusable utility modules handle:

- ADLS path constants
- Secret retrieval from Key Vault
- OAuth configuration
- Source file reading
- Delta writes
- Table registration in Unity Catalog
- Azure SQL connectivity

---

## ADLS Access

Databricks reads from ADLS Gen2 using service principal OAuth credentials stored in a Key Vault-backed Databricks secret scope. No secrets are hardcoded in notebooks.

---

## Custom Source Reader

Source files are headerless CSVs. A custom schema-driven reader handles CDM-style ingestion:

1. Read CDM JSON metadata
2. Build Spark `StructType` schema
3. Read headerless CSV files with the applied schema
4. Write output to Delta Lake

---

## Bronze Layer - Unity Catalog Registration

Raw Delta outputs are registered as managed Bronze tables in Unity Catalog, making them queryable via Spark SQL.

**Bronze tables saved in Unity Catalog:**

![Saved in Bronze Schema in Unity Catalog](../screenshots/Saved_in_bronze_schema_bronze.png)

---

## Silver Layer - Dimensions and Facts

Silver notebooks read from Bronze schemas and produce analytics-ready dimension and fact tables.

**Reading Bronze schema into Silver:**

![Read Bronze Schema into Silver](../screenshots/Read_bronze_schema_silver.png)

**Silver table registered in Unity Catalog:**

![Table Created in Silver Schema in Unity Catalog](../screenshots/Table_created_in_silver_schema_silver.png)

---

## Data Quality Volumes

Data Quality outputs are written to Databricks volumes:

```
dqcheckresults      →  rule execution result rows
dqcheckbadrecords   →  failed/bad records for investigation
```

---

## Main Databricks Responsibilities

- Read raw source data from ADLS Gen2
- Write Raw Delta datasets
- Register Bronze tables in Unity Catalog
- Build Silver dimensions and facts
- Execute Data Quality rules
- Write DQ results and bad records to volumes
- Support workflow orchestration via Databricks Workflows
