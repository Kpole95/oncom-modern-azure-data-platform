# Known Issues and Fixes

## CDM Connector Compatibility

### Problem

The legacy Spark CDM connector was not reliable in the Databricks runtime used for the project.

### Fix

A custom schema-driven ingestion approach was implemented using CDM JSON metadata and Spark `StructType`.

## Headerless CSV Files

### Problem

Source CSV files did not contain headers.

### Fix

Schemas were read or defined from CDM metadata and applied explicitly during ingestion.

## Mixed Source Layouts

### Problem

Some source entities were stored as folders, while others were direct CSV files.

### Fix

The ingestion utility was adjusted to support both folder-based and file-based layouts.

## ADLS OAuth Configuration

### Problem

Databricks compute restrictions caused Spark filesystem configuration issues.

### Fix

A suitable Databricks compute mode was used, and credentials were read through Key Vault-backed secret scope.

## Duplicate Dimension Keys

### Problem

Power BI requires unique dimension keys, but some dimensions produced duplicates.

### Fix

Deduplication was handled in the Silver layer before exposing tables to reporting.

## Numeric Type Issues

### Problem

Some numeric measures were read as strings.

### Fix

Silver transformations cast measures into proper numeric types before reporting.

## VAT Calculation Ambiguity

### Problem

VAT-related fields required cleanup and interpretation before reporting.

### Fix

Fact logic handled VAT values consistently and defaulted missing values where needed.

## Power BI Date/Time Mismatch

### Problem

Date/time formatting caused relationship and time-intelligence issues.

### Fix

The final model kept stable key-based relationships for production-style reporting.

## ADF Metadata Migration Issues

### Problem

Dynamic metadata migration caused errors around duplicate keys, variable usage, and stored procedure parameters.

### Fix

ADF pipeline logic was corrected with proper execution order, parameter mapping, and sequential handling where needed.

## Logic App Content-Type Error

### Problem

Azure DevOps REST API rejected the request because the wrong content type was used.

### Fix

The HTTP action used:

application/json-patch+json

