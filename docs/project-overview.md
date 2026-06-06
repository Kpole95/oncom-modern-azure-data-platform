# Project Overview

## Purpose

The Oncom Modern Azure Data Platform is an Azure Data Engineering project built around a global e-commerce and business operations dataset.

The goal of the project is to build a practical lakehouse platform that can ingest source data, process it through Raw, Bronze, and Silver layers, prepare curated data for Power BI reporting, and validate data quality using a metadata-driven framework.

The project demonstrates real Azure Data Engineering work across storage, compute, orchestration, transformation, reporting, DevOps, and Data Quality.

## Business Domains

The platform covers three business domains:

* **Purchase**: vendors, parties, purchase orders, purchase items, purchase categories, cost centers, currency, and calendar/fiscal dates.
* **Sales**: customers, promotions, payment types, sales order lines, VAT, discounts, and sales amounts.
* **HR**: workers, departments/verticals, employment details, and compensation attributes.

A fourth technical domain supports the project:

* **Data Quality**: metadata-driven validation rules, SQL metadata migration, Databricks rule execution, bad-record capture, and operational issue tracking.

## Platform Scope

The implemented platform includes:

* ADLS Gen2 source storage
* Databricks Raw ingestion
* Delta Lake Raw storage
* Bronze Delta tables
* Silver dimensions and facts
* Databricks Workflows
* Power BI reporting model
* Azure SQL Data Quality metadata
* Azure Data Factory metadata migration
* Databricks Data Quality execution notebooks
* Logic App / Azure DevOps integration for failed checks

## Main Outcome

The final project represents a complete Azure data platform implementation with both analytical reporting and Data Quality capabilities.

It is designed to show practical Azure Data Engineer skills rather than only notebook-level transformations.
