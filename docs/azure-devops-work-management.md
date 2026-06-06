# Azure DevOps Work Management

## Purpose

Azure DevOps provides source control, backlog planning, work item tracking, branch management, and bug tracking for the project.

DevOps practices were used to show the platform was managed like a real delivery project -  not just a collection of isolated notebooks.

---

## Repository Usage

Azure DevOps Repos were used for:

- Databricks notebook version control
- Azure Data Factory Git integration
- Commit history and change tracking
- Branch-based development workflow
- Project delivery evidence

---

## Work Item Structure

Work was organised as:

```
Epic
  └── Feature / User Story
        └── Task
```

Project areas covered:

- Purchase
- Sales
- HR
- Data Quality
- Databricks Workflows
- Power BI Reporting

---

## Backlog

**Purchase and Sales backlog:**

![Azure DevOps Backlog - Purchase and Sales](../screenshots/azure-devops-backlog-purchase-sales.png)

**Data Quality and Workflows backlog:**

![Azure DevOps Backlog - Data Quality and Workflows](../screenshots/azure-devops-backlog-dq-workflows.png)

---

## Work Item Dashboard

The DevOps dashboard tracks active work items, progress, and delivery status across all project areas.

![Azure DevOps Dashboard](../screenshots/azure-devops-dashboard-work-items.png)

---

## Example Work Items

Tracked work items included:

- Purchase Raw notebook development
- Purchase Bronze notebook development
- Purchase Silver dimensional modeling
- Sales Silver model development
- HR model development
- Data Quality metadata framework design
- Data Quality rule execution notebooks
- Power BI reporting
- Workflow orchestration

---

## Bug Tracking

Failed Data Quality checks are connected to Azure DevOps bug creation through Logic Apps. When a DQ rule fails, a bug is automatically raised for operational follow-up.

Example bug pattern:

```
DQ Rule Failure: PrimaryKeyCheck failed on vendtable
```
