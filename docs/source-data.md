# Source Data

## Source System

The source data follows a Microsoft Dynamics-style export pattern. The project starts from files already available in Azure Data Lake Storage Gen2.

The platform does not build the upstream export process. It focuses on lakehouse ingestion, transformation, validation, and reporting.

## Source Format

The source contains:

* headerless CSV files
* CDM JSON metadata files
* manifest files
* entity-level schema files

Because CSV files do not contain headers, the ingestion layer cannot rely on normal CSV header detection. Schemas must be applied explicitly.

## Source Domains

### Purchase


Parties
PartyAddress
VendTable
PurchContracts
PurchaseOrder
PurchItem
PurchCategory


### Sales

CustTable
PromoTable
SalesOrderLine


### HR

WorkerTable


### Reference / Others

Currency
FiscalPeriod
CostCenter


## Source Reading Strategy

The platform uses a custom schema-driven reader.

The process:


CDM JSON metadata
        ↓
Spark StructType schema
        ↓
Headerless CSV read
        ↓
Delta Lake write


## Why This Matters

The original source format is not immediately analytics-ready. The lakehouse ingestion layer standardizes the files into Delta datasets, making them reliable for downstream Bronze and Silver transformations.
