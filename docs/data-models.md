# Data Models

## Overview

The project builds dimensional models for Purchase, Sales, and HR domains. The Silver layer contains analytics-ready dimensions and facts used for Power BI reporting and Data Quality validation.

---

## Purchase Model

### Dimensions

```
silver.dimdate
silver.dimparty
silver.dimvendor
silver.dimpurchasecategory
silver.dimpurchitem
silver.dimcurrency
silver.dimcostcenter
```

### Fact

```
silver.factpurchaseorder
```

### Purpose

The Purchase model supports reporting on vendors, purchase orders, procurement categories, purchased items, cost centers, currency, and time periods.

### Core Relationships

```
dimvendor[VendorId]             1 → * factpurchaseorder[VendorKey]
dimpurchasecategory[CategoryId] 1 → * factpurchaseorder[CategoryKey]
dimpurchitem[ItemId]            1 → * factpurchaseorder[ItemKey]
dimdate[DateId]                 1 → * factpurchaseorder[OrderDateKey]
```

---

## Sales Model

### Dimensions

```
silver.dimcusttable
silver.dimpromotable
silver.dimpaymenttypes
silver.dimdate
```

### Fact

```
silver.factsalesorderline
```

### Purpose

The Sales model supports analysis of customers, payment types, promotions, sales order lines, sales amounts, VAT, discounts, and time-based sales behaviour.

---

## HR Model

### Dimensions

```
silver.dimvertical
silver.dimworker
```

### Purpose

The HR model organises worker and department/vertical information for people-related reporting and analysis.

---

## Transformation Patterns

Silver transformations include:

- Trimming text fields
- Normalising timestamps
- Handling nulls and applying default values
- Casting numeric fields to correct types
- Generating surrogate and hash keys
- Deduplicating dimension rows
- Joining lookup and reference data
- Calculating fact measures (totals, VAT, quantities)

---

## Data Modeling Goal

The Silver layer produces stable, clean, analytics-ready tables that can be consumed directly by Power BI and validated by the Data Quality framework without further transformation.
