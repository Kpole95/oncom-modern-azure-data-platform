# Power BI Reporting

## Purpose

Power BI is used as the reporting layer for curated Silver data. The report is based on dimensional models built in Databricks.

The main reporting focus is Purchase analytics, supported by vendor, category, item, date, and fact purchase order data.

## Report Pages

The report includes pages such as:

* Home
* Vendor Detail
* Category Detail
* Time Series

## Purchase Model

The Purchase report uses `factpurchaseorder` as the central fact table.

Core relationships:

dimvendor[VendorId]                  1 → * factpurchaseorder[VendorKey]
dimpurchasecategory[CategoryId]      1 → * factpurchaseorder[CategoryKey]
dimpurchitem[ItemId]                 1 → * factpurchaseorder[ItemKey]
dimdate[DateId]                      1 → * factpurchaseorder[OrderDateKey]


## Sales Model

The Sales model uses `factsalesorderline` with customer, promotion, payment type, and date dimensions.

## Key Measures

### DAX
Total Purchase Amount = SUM(factpurchaseorder[TotalAmount])
Total Purchase Orders = COUNT(factpurchaseorder[PoNumber])
Total Quantity = SUM(factpurchaseorder[Qty])
Total VAT Amount = SUM(factpurchaseorder[VatAmount])


## Reporting Design

The Power BI model uses:

* star-schema relationships
* single-direction filtering
* reusable DAX measures
* separate report pages for different analysis views
* curated Silver tables as reporting input

## Screenshots

Add report screenshots under:

screenshots/powerbi/


Recommended files:

powerbi-home-page.png
powerbi-vendor-detail.png
powerbi-category-detail.png
powerbi-time-series.png
powerbi-model-relationships.png

