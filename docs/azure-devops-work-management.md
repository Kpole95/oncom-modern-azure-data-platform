# Azure DevOps Work Management

## Purpose

Azure DevOps is used for source control, backlog planning, work item tracking, branch management, and bug tracking.

The project uses DevOps practices to show that the platform was managed like a real delivery project, not just as isolated notebooks.

## Repository Usage

Azure DevOps Repos were used for:

* Databricks notebook version control
* Azure Data Factory Git integration
* commit history
* branch-based development
* project tracking evidence

## Work Item Structure

Work was organized using:

Epic
  └── Feature / User Story
        └── Task

Project areas include:

* Purchase
* Sales
* HR
* Data Quality
* Databricks Workflows
* Power BI Reporting

## Example Work Items

Examples of tracked work:

* Purchase Raw notebook development
* Purchase Bronze notebook development
* Purchase Silver dimensional modeling
* Sales Silver model development
* HR model development
* Data Quality metadata framework
* Data Quality rule execution
* Power BI reporting
* Workflow orchestration

## Bug Tracking

Failed Data Quality checks can be connected to Azure DevOps bugs through Logic Apps.

Example bug pattern:

DQ Rule Failure: PrimaryKeyCheck failed on vendtable

## Screenshots

Add Azure DevOps screenshots under:

screenshots/devops/

Recommended files:

azure-devops-backlog-purchase-sales.png
azure-devops-backlog-dq-workflows.png
azure-devops-dashboard-work-items.png
azure-devops-bug-created-from-dq.png
