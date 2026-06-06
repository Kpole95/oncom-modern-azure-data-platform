# Azure Resource Setup

## Resource Group

All project resources were created under a dedicated Azure development resource group:

```
rg-oncom-dev-001
```

This keeps platform resources isolated and easier to manage.

![Azure Resource Group Overview](../screenshots/azure-resource-group-overview.png)

Azure Cost Management was used throughout development to monitor cloud spend and confirm Databricks as the primary cost driver.

![Azure Cost Management](../screenshots/azure-cost-management.png)

---

## Main Azure Resources

| Resource | Purpose |
|---|---|
| Azure Data Lake Storage Gen2 | Stores source files, Delta outputs, and Power BI exports |
| Azure Databricks | Runs PySpark transformations and DQ notebooks |
| Azure Data Factory | Orchestrates metadata migration and pipeline activity |
| Azure SQL Database | Stores Data Quality metadata and results |
| Azure Key Vault | Stores secrets securely |
| Azure DevOps | Source control, work tracking, and bug management |
| Logic Apps | Automates issue creation from failed DQ results |
| Power BI Desktop | Builds the reporting model |

---

## Storage

Storage account:
```
stoncomdev001
```

Container:
```
oaonoperationsdev
```

The storage account uses hierarchical namespace (ADLS Gen2) and acts as the lake storage layer for raw source files, Delta outputs, and DQ result volumes.

---

## Databricks

Databricks is used for:

- Raw ingestion
- Bronze table creation
- Silver transformation logic
- Databricks Workflows orchestration
- Data Quality execution notebooks
- Delta Lake table operations

---

## Azure SQL Databases

Two Azure SQL databases support the Data Quality framework:

```
sqldb-oncom-dq-temp  →  source metadata database
sqldb-oncom-dq-dev   →  dev metadata and results database
```

---

## Key Vault and Secrets

Credentials are stored in Azure Key Vault and accessed through a Databricks secret scope.

Secret scope:
```
kv-oncom-dev-scope
```

Secrets include service principal credentials and SQL connection strings. No secrets are hardcoded inside notebooks or version-controlled files.
