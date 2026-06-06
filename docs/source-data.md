# Source Data

## Source System

The source data follows a Microsoft Dynamics-style export pattern. The project starts from files already present in Azure Data Lake Storage Gen2.

The platform does not build the upstream export process — it focuses on lakehouse ingestion, transformation, validation, and reporting from those files.

---

## Source Format

The source contains:

- Headerless CSV files (no column headers)
- CDM JSON metadata files (schema definitions)
- Manifest files
- Entity-level schema files

Because CSV files contain no headers, the ingestion layer cannot use normal CSV header detection. Schemas must be applied explicitly from CDM metadata.

---

## Source Domains

### Purchase

```
Parties
PartyAddress
VendTable
PurchContracts
PurchaseOrder
PurchItem
PurchCategory
```

### Sales

```
CustTable
PromoTable
SalesOrderLine
```

### HR

```
WorkerTable
```

### Reference / Others

```
Currency
FiscalPeriod
CostCenter
```

---

## Source Reading Strategy

The platform uses a custom schema-driven reader to handle headerless CDM-style source files:

```
CDM JSON metadata
        │
        ▼
Spark StructType schema
        │
        ▼
Headerless CSV read
        │
        ▼
Delta Lake write
```

---

## Why This Matters

The source format is not immediately analytics-ready. The lakehouse ingestion layer standardises these files into reliable Delta datasets, providing a stable foundation for Bronze and Silver transformations downstream.
