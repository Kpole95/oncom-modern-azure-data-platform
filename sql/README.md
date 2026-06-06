# SQL — Metadata-Driven Data Quality Framework

This folder contains SQL scripts for the Data Quality framework of the Oncom Modern Azure Data Platform. Scripts cover schema creation, metadata configuration, stored procedures, and supporting views used by Databricks and Logic Apps.

---

## Folder Structure

```
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
```

---

## Databases Used

Two Azure SQL databases support the framework:

| Database | Role |
|---|---|
| `sqldb-oncom-dq-temp` | Source metadata database — holds original DQ metadata |
| `sqldb-oncom-dq-dev` | Dev database — holds migrated metadata, incremental mappings, DQ results, views, and procedures |

---

## Execution Order

Scripts must be run in the order below to avoid foreign key and object dependency errors.

**Source database (`sqldb-oncom-dq-temp`):**

1. `ddl/01_create_dqr_schema.sql`
2. `ddl/02_create_dq_metadata_tables_source.sql`
3. `config/01_insert_source_dq_metadata.sql`

**Dev database (`sqldb-oncom-dq-dev`):**

1. `ddl/01_create_dqr_schema.sql`
2. `ddl/03_create_dq_metadata_tables_dev.sql`
3. `ddl/04_create_dqresults_table.sql`
4. `config/02_insert_dev_incremental_mappings.sql`
5. `config/03_insert_dqresults_watermark.sql`
6. `procedures/01_create_sp_update_watermark.sql`
7. `views/01_create_vw_rules.sql`
8. `views/02_create_vw_dq_failed_results.sql`

---

## Main Objects

| Object | Purpose |
|---|---|
| `dqr.dqchecks` | Stores data quality check types such as primary key, null, record count, and sum checks |
| `dqr.dqobjects` | Stores lakehouse tables and objects registered for validation |
| `dqr.dqrules` | Maps rules to objects, layers, attributes, and SQL validation logic |
| `dqr.incremental_load_mappings` | Tracks incremental metadata loads and watermark values |
| `dqr.dqresults` | Stores DQ execution results written by Databricks notebooks |
| `dqr.sp_UpdateWatermark` | Updates watermark values after each incremental run |
| `dqr.Vw_Rules` | Provides executable rule metadata to Databricks notebooks |
| `dqr.Vw_DQ_Failed_Results` | Returns failed DQ results for monitoring and bug ticket creation |

---

## How It Is Used

1. DQ metadata is inserted into the source database (`sqldb-oncom-dq-temp`).
2. Azure Data Factory migrates metadata incrementally into the dev database (`sqldb-oncom-dq-dev`).
3. Databricks reads `dqr.Vw_Rules` and executes validation rules against Bronze and Silver tables.
4. Execution results are written to `dqr.dqresults`.
5. Failed results are exposed through `dqr.Vw_DQ_Failed_Results`.
6. Logic Apps or Azure DevOps consume failed results to create bug tickets for operational follow-up.

---

## Validation Queries

```sql
SELECT * FROM dqr.dqchecks;
SELECT * FROM dqr.dqobjects;
SELECT * FROM dqr.dqrules;
SELECT * FROM dqr.incremental_load_mappings;
SELECT * FROM dqr.dqresults;
SELECT * FROM dqr.Vw_Rules;
SELECT * FROM dqr.Vw_DQ_Failed_Results;
```

---

## Notes

- Scripts are designed for **Azure SQL Database** — do not use `USE database_name` statements; connect directly to the target database.
- Follow the execution order strictly to avoid dependency errors between objects.
- Views depend on `dqresults` and `incremental_load_mappings` being created first.
- The stored procedure updates watermark values after each incremental ADF run.
- Do not commit credentials, PATs, or connection strings to this folder.