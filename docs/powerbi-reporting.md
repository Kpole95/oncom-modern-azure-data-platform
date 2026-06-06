# Power BI Reporting

## Purpose

Power BI serves as the reporting layer for curated Silver data. The report is built on dimensional models produced in Databricks and follows a star-schema structure with fact tables connected to dimension tables.

The main reporting focus is Purchase analytics, supported by vendor, category, item, date, and fact purchase order data.

---

## Report Pages

### Home Dashboard

Top-level KPIs and summary visuals covering overall purchase activity, total amounts, order counts, and quantity trends.

![Home Dashboard](../screenshots/HomeDashboard.png)

### Vendor Detail

Per-vendor breakdown of purchase amounts, order counts, and item distribution across the selected time period.

![Vendor Detail](../screenshots/VendorDetail.png)

### Category Detail

Purchase performance sliced by procurement category, showing spend distribution and order volume by category.

![Category Detail](../screenshots/CategoryDetail.png)

### Time Series Analysis

Trend analysis of purchase volumes and amounts over fiscal periods, supporting time-based pattern discovery.

![Time Series Analysis](../screenshots/TimeSeriesAnalysis.png)

---

## Purchase Model

The Purchase report uses `factpurchaseorder` as the central fact table.

Core relationships:

```
dimvendor[VendorId]             1 → * factpurchaseorder[VendorKey]
dimpurchasecategory[CategoryId] 1 → * factpurchaseorder[CategoryKey]
dimpurchitem[ItemId]            1 → * factpurchaseorder[ItemKey]
dimdate[DateId]                 1 → * factpurchaseorder[OrderDateKey]
```

---

## Sales Model

The Sales model uses `factsalesorderline` with customer, promotion, payment type, and date dimensions.

---

## Key DAX Measures

```dax
Total Purchase Amount = SUM(factpurchaseorder[TotalAmount])
Total Purchase Orders = COUNT(factpurchaseorder[PoNumber])
Total Quantity        = SUM(factpurchaseorder[Qty])
Total VAT Amount      = SUM(factpurchaseorder[VatAmount])
```

---

## Reporting Design

The Power BI model uses:

- Star-schema relationships
- Single-direction filter propagation
- Reusable DAX measures
- Separate report pages for different analysis views
- Curated Silver tables as the semantic reporting source

Time-intelligence experimentation was kept separate from the main report model to prevent breaking production-style visuals.
