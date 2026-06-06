# Project Overview

## Purpose

The Oncom Modern Azure Data Platform is an end-to-end Azure data engineering project built around a fictional global e-commerce and business operations dataset.

The goal is to build a practical lakehouse platform that ingests source data, processes it through Raw, Bronze, and Silver layers, prepares curated data for Power BI reporting, and validates data quality using a metadata-driven framework.

The project demonstrates real Azure Data Engineering work across storage, compute, orchestration, transformation, reporting, DevOps delivery, and Data Quality.

---

## Business Domains

The platform covers three business domains:

- **Purchase** - vendors, parties, purchase orders, purchase items, purchase categories, cost centers, currency, and calendar/fiscal dates
- **Sales** - customers, promotions, payment types, sales order lines, VAT, discounts, and sales amounts
- **HR** - workers, departments/verticals, employment details, and compensation attributes

A fourth technical domain supports platform operations:

- **Data Quality** - metadata-driven validation rules, SQL metadata migration, Databricks rule execution, bad-record capture, and operational issue tracking

---

## Platform Scope

The implemented platform includes:

| Component | Description |
|---|---|
| ADLS Gen2 | Source and Delta storage |
| Databricks Raw | CDM/CSV ingestion to Delta |
| Delta Lake | Raw, Bronze, and Silver storage |
| Bronze Tables | Unity Catalog registered tables |
| Silver Layer | Analytics-ready dimensions and facts |
| Databricks Workflows | Notebook orchestration |
| Power BI | Star-schema reporting model |
| Azure SQL | Data Quality metadata store |
| Azure Data Factory | Incremental metadata migration |
| Databricks DQ Notebooks | Rule execution and bad-record capture |
| Logic App / Azure DevOps | Failed check issue tracking |

---

## Main Outcome

The final project represents a complete Azure data platform implementation with both analytical reporting and operational Data Quality capabilities.

It is designed to demonstrate practical Azure Data Engineer skills - including cloud infrastructure, secure access patterns, lakehouse design, PySpark transformations, orchestration, and reporting - rather than only notebook-level work.
