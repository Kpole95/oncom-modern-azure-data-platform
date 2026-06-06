# Data Quality Framework

## Purpose

The Data Quality framework validates lakehouse data using metadata-driven rules. Rather than hardcoding checks directly in notebooks, rule configuration is stored in Azure SQL and executed dynamically in Databricks.

This makes the framework easier to extend, audit, and operate without modifying notebook code.

---

## Main Components

| Component | Purpose |
|---|---|
| Azure SQL Metadata Tables | Store checks, objects, rules, and watermarks |
| Azure Data Factory | Migrates metadata incrementally |
| Databricks DQ Notebooks | Execute validation rules against lakehouse tables |
| Databricks Volumes | Store result files and bad records |
| SQL Views | Expose rules and failed results for consumption |
| Logic Apps / Azure DevOps | Support issue tracking for failed checks |

---

## SQL Metadata Objects

```
dqr.dqchecks                 →  data quality check types such as primary key, null, record count, and sum checks
dqr.dqobjects                →  registered lakehouse objects
dqr.dqrules                  →  rule definitions and parameters
dqr.incremental_load_mappings →  watermark tracking
dqr.dqresults                →  execution result rows
dqr.Vw_Rules                 →  consolidated rule view for execution
dqr.Vw_DQ_Failed_Results     →  failed validation results for review
dqr.sp_UpdateWatermark        →  stored procedure for watermark updates
```

---

## Rule Execution Flow

```
DQ metadata source (Azure SQL)
        │
        ▼
ADF incremental migration
        │
        ▼
DQ metadata dev database
        │
        ▼
Databricks reads dqr.Vw_Rules
        │
        ▼
Databricks executes rules against lakehouse tables
        │
        ▼
Results written to dqr.dqresults
        │
        ▼
Bad records written to Databricks volume
        │
        ▼
Failed rows exposed via dqr.Vw_DQ_Failed_Results
```

**DQ rule execution in Databricks:**

![Databricks DQ Rule Execution](../screenshots/databricks-dq-rule-execution.png)

---

## Rule Types

The metadata model supports:

- **Primary Key checks** - verify uniqueness of key columns
- **Null checks** - detect unexpected null values in required fields
- **Record count checks** - compare row counts across layers or time windows
- **Sum checks** - validate aggregated measure totals

---

## Bad Record Handling

When a rule fails, the framework persists the failed records into a dedicated bad-record volume (`dqcheckbadrecords`). This makes failures investigable at the row level rather than only showing pass/fail counts.

---

## Operational Use

Failed DQ results feed into:

- Monitoring dashboards
- Operational review processes
- Azure DevOps bug creation via Logic Apps
- Pipeline failure investigation
