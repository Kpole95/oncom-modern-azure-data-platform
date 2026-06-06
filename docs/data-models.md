# Data Models

## Overview

The project builds dimensional models for Purchase, Sales, and HR domains. The Silver layer contains analytics-ready dimensions and facts used for reporting and Data Quality validation.

## Purchase Model

### Dimensions

silver.dimdate
silver.dimparty
silver.dimvendor
silver.dimpurchasecategory
silver.dimpurchitem
silver.dimcurrency
silver.dimcostcenter


### Fact

silver.factpurchaseorder


### Purchase Model Purpose

The Purchase model supports reporting on vendors, purchase orders, purchase categories, purchased items, cost centers, currency, and time periods.

### Core Purchase Relationships

dimvendor[VendorId]                  1 → * factpurchaseorder[VendorKey]
dimpurchasecategory[CategoryId]      1 → * factpurchaseorder[CategoryKey]
dimpurchitem[ItemId]                 1 → * factpurchaseorder[ItemKey]
dimdate[DateId]                      1 → * factpurchaseorder[OrderDateKey]


## Sales Model

### Dimensions

silver.dimcusttable
silver.dimpromotable
silver.dimpaymenttypes
silver.dimdate


### Fact

silver.factsalesorderline


### Sales Model Purpose

The Sales model supports analysis of customers, payment types, promotions, sales order lines, sales amounts, VAT, discounts, and time-based sales behavior.

## HR Model

### Dimensions

silver.dimvertical
silver.dimworker


### HR Model Purpose

The HR model organizes worker and department/vertical information for people-related reporting and analysis.

## Transformation Patterns

Silver transformations include:

* trimming text fields
* normalizing timestamps
* handling nulls
* applying default dates
* casting numeric fields
* generating keys
* deduplicating dimension rows
* joining lookup/reference data
* calculating fact measures

## Data Modeling Goal

The goal of the Silver layer is to produce stable, clean, analytics-ready tables that can be consumed by Power BI and validated by the Data Quality framework.
