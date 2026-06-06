# SQL Folder – Metadata-Driven Data Quality Framework

This folder contains SQL scripts for the **Data Quality framework** of the Oncom Modern Azure Data Platform. It is designed for project setup, data quality metadata, and supporting views/procedures.

The folder structure:

```text
sql/
├── ddl/
│   ├── 01_create_dqr_schema.sql
│   ├── 02_create_dq_metadata_tables_source.sql
│   ├── 03_create_dq_metadata_tables_dev.sql
│   └── 04_create_dqresults_table.sql
├── config/
│   ├── 01_insert_source_dq_metadata.sql
│   ├── 02_insert_dev_incremental_mappings.sql
│   └── 03_insert_dqresults_watermark.sql
├── procedures/
│   └── 01_create_sp_update_watermark.sql
└── views/
    ├── 01_create_vw_rules.sql
    └── 02_create_vw_dq_failed_results.sql


# Purpose

The SQL scripts support the Data Quality framework by creating:

dqr schema
Metadata tables for checks, objects, and rules
Incremental load mapping tables
DQ execution result tables
Stored procedure for watermark updates
Views for Databricks execution
Views for failed results used by Logic Apps or Azure DevOps

# Databases Used

Two Azure SQL databases:

sqldb-oncom-dq-temp → Source metadata database
sqldb-oncom-dq-dev → Development metadata & execution results

temp holds original metadata; dev holds migrated metadata, incremental mappings, DQ results, and supporting views/procedures.


# Execution Order

Source Database (sqldb-oncom-dq-temp):
1. ddl/01_create_dqr_schema.sql
2. ddl/02_create_dq_metadata_tables_source.sql
3. config/01_insert_source_dq_metadata.sql

Development Database (sqldb-oncom-dq-dev):
1. ddl/01_create_dqr_schema.sql
2. ddl/03_create_dq_metadata_tables_dev.sql
3. ddl/04_create_dqresults_table.sql
4. config/02_insert_dev_incremental_mappings.sql
5. config/03_insert_dqresults_watermark.sql
6. procedures/01_create_sp_update_watermark.sql
7. views/01_create_vw_rules.sql
8. views/02_create_vw_dq_failed_results.sql



# Main objects

| Object                          | Purpose                                                                  |
| ------------------------------- | ------------------------------------------------------------------------ |
| `dqr.dqchecks`                  | Stores types of Data Quality checks: Primary Key, Null, Count, Sum, etc. |
| `dqr.dqobjects`                 | Stores lakehouse tables and objects for validation.                      |
| `dqr.dqrules`                   | Maps rules to objects, layers, attributes, and SQL validation logic.     |
| `dqr.incremental_load_mappings` | Tracks incremental metadata loads and watermarks.                        |
| `dqr.dqresults`                 | Stores Data Quality execution results from Databricks.                   |
| `dqr.sp_UpdateWatermark`        | Updates watermark values after incremental runs.                         |
| `dqr.Vw_Rules`                  | Provides executable rule metadata to Databricks notebooks.               |
| `dqr.Vw_DQ_Failed_Results`      | Returns failed DQ results for monitoring and bug ticket creation.        |


# How it is used:

1. How It Is Used
2. Metadata inserted into source database (temp).
3. Azure Data Factory migrates metadata into development database (dev) incrementally.
4. Databricks reads dqr.Vw_Rules and executes rules against Bronze/Silver tables.
5. Execution results written to dqr.dqresults.
6. Failed results appear in dqr.Vw_DQ_Failed_Results.
7. Logic Apps or Azure DevOps can create bug tickets for failed rows.

# Validation Queries

SELECT * FROM dqr.dqchecks;
SELECT * FROM dqr.dqobjects;
SELECT * FROM dqr.dqrules;
SELECT * FROM dqr.incremental_load_mappings;
SELECT * FROM dqr.dqresults;
SELECT * FROM dqr.Vw_Rules;
SELECT * FROM dqr.Vw_DQ_Failed_Results;


# Notes

Scripts are designed for Azure SQL Database.
Connect directly to the target database; do not use USE database_name.
Do not commit credentials, PATs, or secrets.
Follow the execution order to avoid foreign key and object errors.
Views depend on dqresults and incremental mapping tables.
Stored procedures update watermark values after incremental runs.
Treat this folder as a professional, portfolio-ready SQL setup for Data Quality.