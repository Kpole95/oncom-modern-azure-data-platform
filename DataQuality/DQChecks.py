# Databricks notebook source
from databricks.sdk.runtime import *
from pyspark.sql import functions as F

# COMMAND ----------

# Use your actual catalog
catalog_name = "dbw_oncom_dev_001_7405615875359132"
dq_schema_name = "dataquality"

bad_records_base_path = f"/Volumes/{catalog_name}/{dq_schema_name}/dqcheckbadrecords"
check_results_base_path = f"/Volumes/{catalog_name}/{dq_schema_name}/dqcheckresults"


# COMMAND ----------

# Helper function to create rule result
def buildRuleResultDf(objectname, sourcelayer, targetlayer, rulename, sourceresult, targetresult=None):
    targetlayer_sql = "CAST(NULL AS STRING)" if targetlayer is None else f"'{targetlayer}'"
    targetresult_sql = "CAST(NULL AS DECIMAL(20,4))" if targetresult is None else f"CAST({targetresult} AS DECIMAL(20,4))"

    return spark.sql(f"""
        SELECT
            '{objectname}' AS objectname,
            '{sourcelayer}' AS sourcelayer,
            {targetlayer_sql} AS targetlayer,
            '{rulename}' AS rulename,
            CAST({sourceresult} AS DECIMAL(20,4)) AS sourceresult,
            {targetresult_sql} AS targetresult,
            current_timestamp() AS rundatetime
    """)

# COMMAND ----------

# Primary key check
def executePrimaryKeyCheck(objectname, layer, rulename, dqattribute1, sqlquery):
    full_table_name = f"{catalog_name}.{layer}.{objectname}"

    sqlquery_object = sqlquery.replace(objectname, full_table_name)

    print(f"Executing Primary Key Check for {full_table_name}")
    print(sqlquery_object)

    df_dqcheck = spark.sql(sqlquery_object)

    if df_dqcheck.isEmpty():
        df_dqcheck_result = buildRuleResultDf(
            objectname=objectname,
            sourcelayer=layer,
            targetlayer=None,
            rulename=rulename,
            sourceresult=1
        )

    else:
        df_dqcheck_result = buildRuleResultDf(
            objectname=objectname,
            sourcelayer=layer,
            targetlayer=None,
            rulename=rulename,
            sourceresult=0
        )

        df_bad_records = (
            spark.table(full_table_name)
            .join(df_dqcheck, dqattribute1, "inner")
        )

        (
            df_bad_records.write
            .mode("append")
            .format("csv")
            .option("header", "true")
            .option("path", f"{bad_records_base_path}/{objectname}/{rulename}/")
            .save()
        )

    display(df_dqcheck_result)

    (
        df_dqcheck_result.write
        .mode("append")
        .format("csv")
        .option("header", "true")
        .option("path", f"{check_results_base_path}/{objectname}/{rulename}/")
        .save()
    )

# COMMAND ----------

# Null check
def executeNullCheck(objectname, layer, rulename, dqattribute1, sqlquery):
    full_table_name = f"{catalog_name}.{layer}.{objectname}"

    sqlquery_object = sqlquery.replace(objectname, full_table_name)

    print(f"Executing Null Check for {full_table_name}.{dqattribute1}")
    print(sqlquery_object)

    df_dqcheck = spark.sql(sqlquery_object)

    if df_dqcheck.isEmpty():
        df_dqcheck_result = buildRuleResultDf(
            objectname=objectname,
            sourcelayer=layer,
            targetlayer=None,
            rulename=rulename,
            sourceresult=1
        )

    else:
        df_dqcheck_result = buildRuleResultDf(
            objectname=objectname,
            sourcelayer=layer,
            targetlayer=None,
            rulename=rulename,
            sourceresult=0
        )

        df_bad_records = spark.sql(f"""
            SELECT *
            FROM {full_table_name}
            WHERE {dqattribute1} IS NULL
        """)

        (
            df_bad_records.write
            .mode("append")
            .format("csv")
            .option("header", "true")
            .option("path", f"{bad_records_base_path}/{objectname}/{rulename}/")
            .save()
        )

    display(df_dqcheck_result)

    (
        df_dqcheck_result.write
        .mode("append")
        .format("csv")
        .option("header", "true")
        .option("path", f"{check_results_base_path}/{objectname}/{rulename}/")
        .save()
    )
