# Silver Notebooks - Standardized Markdown

This folder contains the Silver layer notebooks with standardized markdown documentation.

The executable code has been preserved. Markdown cells were standardized so each notebook follows the same professional structure:

1. Silver transformation overview
2. Shared library setup
3. Source table reads
4. Schema/source validation
5. Silver transformation logic
6. Final DataFrame assignment
7. Write to Silver schema
8. Optional post-write validation where already present

`dimcostcenter_silver.py` was uploaded as a Databricks notebook source file. A cleaned `.py` version and a converted `.ipynb` version are both included.

## Files


- `dimcostcenter_silver.ipynb` — `dimcostcenter` (ipynb)
- `dimcurrency_silver.ipynb` — `dimcurrency` (ipynb)
- `dimcusttable_silver.ipynb` — `dimcusttable` (ipynb)
- `dimdate_silver.ipynb` — `dimdate` (ipynb)
jc- `dimparty_silver.ipynb` — `dimparty` (ipynb)
- `dimpaymenttypes_silver.ipynb` — `dimpaymenttypes` (ipynb)
- `dimpromotable_silver.ipynb` — `dimpromotable` (ipynb)
- `dimpurchcategory_silver.ipynb` — `dimpurchasecategory` (ipynb)
- `dimpurchitem_silver.ipynb` — `dimpurchitem` (ipynb)
- `dimvendor_silver.ipynb` — `dimvendor` (ipynb)
- `dimvertical_silver.ipynb` — `dimvertical` (ipynb)
- `dimworker_silver.ipynb` — `dimworker` (ipynb)
- `factpurchaseorder_silver.ipynb` — `factpurchaseorder` (ipynb)
- `factsalesorderline_silver.ipynb` — `factsalesorderline` (ipynb)
