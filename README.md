# Oncom Modern Azure Data Platform

## Overview

Oncom Modern Azure Data Platform is an end-to-end Azure Data Engineering project built around a fictional global e-commerce and business operations dataset. The platform ingests Microsoft Dynamics-style CDM/CSV exports from Azure Data Lake Storage Gen2, processes the data through a lakehouse medallion architecture, builds analytics-ready dimensional models in Azure Databricks, orchestrates notebook execution through Databricks Workflows, supports metadata-driven data quality validation, and serves curated reporting data into Power BI.

The project demonstrates practical data engineering work across cloud infrastructure, secure storage access, PySpark transformations, Delta Lake table design, Azure DevOps source control, workflow orchestration, Power BI modeling, and data quality engineering.

---

## Business Domains

The platform covers three business domains:

- **Purchase**: vendors, parties, purchase orders, purchase items, purchase categories, currency, cost centers, and fiscal/calendar dates.
- **Sales**: customers, promotions, payment types, sales order lines, discounts, VAT, and sales order amounts.
- **HR**: workers, verticals/departments, employment details, and compensation attributes.

A fourth technical domain supports the platform:

- **Data Quality**: metadata-driven rule configuration, SQL metadata migration, rule execution patterns, validation result handling, bad-record capture, and operational issue tracking.

---

## Architecture

```text
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
```

The reporting path uses the Silver layer directly as the curated semantic source for Power BI. A separate Data Quality path uses SQL metadata and Databricks execution notebooks to validate data across lakehouse layers.

## Technology Stack

| Area | Technologies |
|---|---|
| Cloud Platform | Microsoft Azure |
| Storage | ADLS Gen2 |
| Processing | Azure Databricks, PySpark, Spark SQL |
| Table Format | Delta Lake |
| Orchestration | Databricks Workflows, Azure Data Factory |
| Metadata Store | Azure SQL Database |
| Secrets | Azure Key Vault, Databricks Secret Scope |
| DevOps | Azure DevOps Repos, Branches, Work Items |
| Reporting | Power BI Desktop |
| Languages | Python, PySpark, SQL, DAX |
| Data Quality | Metadata-driven SQL rules, rule execution notebooks, validation outputs |

## Repository Structure

.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── azure-devops-work-management.md
│   ├── data-models.md
│   ├── data-quality-framework.md
│   ├── databricks-setup.md
│   ├── known-issues-and-fixes.md
│   ├── powerbi-reporting.md
│   ├── project-log.md
│   ├── project-overview.md
│   ├── resource-setup.md
│   └── source-data.md
├── notes/
│   ├── adls-oauth-utility.md
│   ├── cdm-read-poc.md
│   ├── databricks-setup.md
│   ├── final-project-summary.md
│   ├── github-push-guide.md
│   ├── issues-and-blockers.md
│   ├── lecture-notes.md
│   └── readme.md
├── notebooks/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   ├── data_quality/
│   └── workflows/
├── screenshots/
│   ├── azure/
│   ├── databricks/
│   ├── devops/
│   ├── dq/
│   └── powerbi/
└── sql/
    ├── ddl/
    ├── config/
    ├── procedures/
    └── views/

## Implemented Lakehouse Layers

### Raw Layer

The Raw layer ingests CDM-style headerless CSV files from ADLS Gen2 and stores them as Delta Lake datasets. Because the source files do not contain headers, the ingestion framework reads schema metadata from CDM JSON files and applies explicit Spark schemas before loading the data

Raw ingestion was implemented for:

- Purchase: `Parties`, `PartyAddress`, `VendTable`, `PurchContracts`, `PurchaseOrder`, `PurchItem`, `PurchCategory`
- Sales: `CustTable`, `PromoTable`, `SalesOrderLine`
- HR: `WorkerTable`
- Reference/Others: `Currency`, `FiscalPeriod`, `CostCenter`

### Bronze Layer

The Bronze layer registers Raw Delta outputs as Databricks tables. Bronze keeps the source-like structure while making data queryable through Spark SQL and available for downstream transformations.

Bronze tables include:

- `bronze.parties`
- `bronze.partyaddress`
- `bronze.vendtable`
- `bronze.purchaseorder`
- `bronze.purchitem`
- `bronze.purchcategory`
- `bronze.purchcontracts`
- `bronze.custtable`
- `bronze.promotable`
- `bronze.salesorderline`
- `bronze.workertable`
- `bronze.currency`
- `bronze.fiscalperiod`
- `bronze.costcenter`

### Silver Layer

The Silver layer creates analytics-ready dimensions and facts. Transformations include trimming text, timestamp normalization, default date handling, null handling, type casting, business key selection, deduplication, hash-key creation, lookup enrichment, and fact-table calculations.

Silver tables include:

- `silver.dimdate`
- `silver.dimparty`
- `silver.dimvendor`
- `silver.dimpurchasecategory`
- `silver.dimpurchitem`
- `silver.dimcurrency`
- `silver.dimcostcenter`
- `silver.factpurchaseorder`
- `silver.dimcusttable`
- `silver.dimpromotable`
- `silver.dimpaymenttypes`
- `silver.factsalesorderline`
- `silver.dimvertical`
- `silver.dimworker`

## Power BI Reporting

The Power BI model uses star-schema modeling over the Silver layer. The report includes pages such as Home, Vendor Detail, Category Detail, and Time Series. The model uses dimension-to-fact relationships, single-direction filtering, and reusable DAX measures.

Core Purchase relationships:

dimvendor[VendorId]                  1 → * factpurchaseorder[VendorKey]
dimpurchasecategory[CategoryId]      1 → * factpurchaseorder[CategoryKey]
dimpurchitem[ItemId]                 1 → * factpurchaseorder[ItemKey]
dimdate[DateId]                      1 → * factpurchaseorder[OrderDateKey]

Key measures:
DAX:
Total Purchase Amount = SUM(factpurchaseorder[TotalAmount])
Total Purchase Orders = COUNT(factpurchaseorder[PoNumber])
Total Quantity = SUM(factpurchaseorder[Qty])
Total VAT Amount = SUM(factpurchaseorder[VatAmount])

## Report Screenshots

## Data Quality Framework

The Data Quality layer uses SQL metadata tables to define rules and Databricks notebooks to execute checks against lakehouse tables. The metadata model supports multiple rule types including primary key checks, record count comparisons, sum checks, and null checks.

Core SQL metadata objects:

- dqr.dqchecks
- dqr.dqobjects
- dqr.dqrules
- dqr.incremental_load_mappings
- dqr.sp_UpdateWatermark
- dqr.Vw_Rules
- dqr.Vw_DQ_Failed_Results


Operational flow:

DQ metadata source
        |
        v
ADF incremental migration
        |
        v
Dev metadata database
        |
        v
Databricks DQ rule execution
        |
        v
DQ result and bad-record outputs
        |
        v
Failed-results view
        |
        v
Logic App / Azure DevOps bug tracking


## Key Engineering Decisions

### Replaced Legacy CDM Connector

The initial ingestion design expected a Spark CDM connector. The connector was not reliable in the target Databricks runtime, so the platform uses a custom schema-driven ingestion approach:

CDM JSON metadata
        |
        v
Dynamic Spark StructType
        |
        v
Headerless CSV read
        |
        v
Delta Lake output

This made the ingestion independent of connector/runtime compatibility issues.

### Used Databricks Secret Scope

Credentials are not hardcoded. ADLS and SQL access use Key Vault-backed Databricks secrets.

### Used Silver-Layer Deduplication

Dimension keys used in Power BI must be unique. Duplicate handling was implemented in the Silver layer for dimensions such as date, vendor, party, and purchase category.

### Kept Power BI Model Stable

The final Power BI relationship model prioritizes stable star-schema relationships and correct visual behavior. Time-intelligence experimentation was handled separately from the main report model to avoid breaking production-style visuals.

## Main Problems Solved

CDM connector compatibility failure
Headerless CSV ingestion
Mixed source layouts: entity folders and direct CSV files
ADLS OAuth configuration errors
Databricks compute restrictions for Spark filesystem configs
Duplicate DateId in dimdate
Duplicate business keys in dimensions
Delta schema mismatch during type changes
TotalOrder stored as text instead of numeric
VAT percentage vs VAT amount ambiguity
Payment types derived from transactional data
Power BI relationship direction errors
Power BI date/time relationship mismatch
ADF dynamic metadata migration issues
DQ bad-record capture and failed-result handling
Logic App integration with Azure DevOps REST API

## Professional Summary

This project demonstrates a complete Azure Data Engineering workflow: cloud resource setup, secure storage access, data ingestion, medallion architecture, Delta Lake modeling, PySpark transformation logic, Databricks workflow orchestration, SQL metadata management, data quality validation, Azure DevOps delivery practices, and Power BI reporting.

It is designed as a practical portfolio project for Azure Data Engineer, Data