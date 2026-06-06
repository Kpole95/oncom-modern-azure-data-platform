# Data Quality Framework

## Purpose

The Data Quality framework validates lakehouse data using metadata-driven rules. Instead of hardcoding every rule directly in notebooks, rule configuration is stored in Azure SQL and executed dynamically in Databricks.

This makes the framework easier to extend, audit, and operate.

## Main Components

| Component                 | Purpose                                      |
| ------------------------- | -------------------------------------------- |
| Azure SQL Metadata Tables | Store checks, objects, rules, and watermarks |
| Azure Data Factory        | Migrates metadata incrementally              |
| Databricks DQ Notebooks   | Execute validation rules                     |
| Databricks Volumes        | Store result files and bad records           |
| SQL Views                 | Expose rules and failed results              |
| Logic Apps / Azure DevOps | Support issue tracking for failed checks     |

## SQL Metadata Objects

dqr.dqchecks
dqr.dqobjects
dqr.dqrules
dqr.incremental_load_mappings
dqr.dqresults
dqr.Vw_Rules
dqr.Vw_DQ_Failed_Results
dqr.sp_UpdateWatermark


## Rule Execution Flow

DQ metadata source
        ↓
ADF incremental migration
        ↓
DQ metadata dev database
        ↓
Databricks reads dqr.Vw_Rules
        ↓
Databricks executes rules
        ↓
Results written to dqr.dqresults
        ↓
Bad records written to Databricks volume
        ↓
Failed rows exposed through dqr.Vw_DQ_Failed_Results


## Rule Types

The metadata model supports rule types such as:

* Primary Key checks
* Null checks
* Record count checks
* Sum checks

## Bad Record Handling

When a rule fails, the framework can persist failed records into a dedicated bad-record volume. This makes failures easier to investigate instead of only showing pass/fail numbers.

## Operational Use

Failed DQ results can be used for:

* monitoring
* dashboards
* operational review
* Azure DevOps bug creation
* pipeline failure investigation
