# Known Issues and Fixes

## CDM Connector Compatibility

**Problem:** The legacy Spark CDM connector was not reliable on the Databricks runtime used for the project.

**Fix:** A custom schema-driven ingestion approach was implemented using CDM JSON metadata and Spark `StructType`. This eliminated connector and runtime compatibility issues entirely.

---

## Headerless CSV Files

**Problem:** Source CSV files did not contain column headers, so normal CSV header detection could not be used.

**Fix:** Schemas were read from CDM metadata files and applied explicitly during ingestion via a custom reader.

---

## Mixed Source Layouts

**Problem:** Some source entities were stored as entity folders, while others were direct CSV files, requiring different path handling.

**Fix:** The ingestion utility was updated to support both folder-based and file-based layouts dynamically.

---

## ADLS OAuth Configuration

**Problem:** Databricks compute restrictions caused Spark filesystem configuration issues when setting OAuth credentials.

**Fix:** A compatible Databricks compute mode was used, and credentials were retrieved through a Key Vault-backed Databricks secret scope rather than set at the session level.

---

## Duplicate Dimension Keys

**Problem:** Power BI requires unique dimension keys for valid relationships, but some dimensions produced duplicate key values.

**Fix:** Deduplication was implemented in the Silver layer before dimension tables were exposed to reporting.

---

## Numeric Type Issues

**Problem:** Some numeric measures (e.g. `TotalOrder`) were ingested as string type.

**Fix:** Silver transformations explicitly cast affected columns to the correct numeric types before reporting.

---

## VAT Calculation Ambiguity

**Problem:** VAT-related fields required interpretation — distinguishing VAT percentage from VAT amount caused inconsistencies.

**Fix:** Fact logic was updated to handle VAT values consistently, with explicit defaults where values were missing.

---

## Power BI Date/Time Mismatch

**Problem:** Date/time field formatting caused relationship and time-intelligence issues in the Power BI model.

**Fix:** The model was simplified to use stable key-based date relationships for production visuals. Time-intelligence experimentation was isolated from the main report.

---

## ADF Metadata Migration Issues

**Problem:** Dynamic metadata migration in ADF caused errors around duplicate keys, variable scoping, and stored procedure parameter handling.

**Fix:** Pipeline logic was corrected with proper execution order, parameter mapping, and sequential activity handling.

---

## Logic App Content-Type Error

**Problem:** The Azure DevOps REST API rejected Logic App requests due to an incorrect `Content-Type` header.

**Fix:** The HTTP action was updated to use:

```
Content-Type: application/json-patch+json
```
