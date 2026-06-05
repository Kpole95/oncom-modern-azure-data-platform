# Databricks notebook source
from databricks.sdk.runtime import *

# COMMAND ----------

# MAGIC %run /Workspace/Repos/krishnapole95s@gmail.com/modern-dw-databricks/DataQuality/Utilities

# COMMAND ----------

# MAGIC %run /Workspace/Repos/krishnapole95s@gmail.com/modern-dw-databricks/DataQuality/DQChecks

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, TimestampType

# COMMAND ----------

# Read all DQ rules
df_rules = ReadTableFromDatabase("dqr.Vw_Rules")
display(df_rules)
display(df_rules.select("dqrulename").distinct())

# COMMAND ----------

# Execute each rule
for row in df_rules.collect():
    object_name = row["dqobjectname"]
    sourcelayer = row["sourcelayer"]
    targetlayer = row["targetlayer"]
    rulename = row["dqrulename"]
    sqlquery = row["sqlquery"]
    sourceattr = row["dqattribute1"]

    rule_name_norm = rulename.replace(" ", "").replace("_", "").lower()

    if "primary" in rule_name_norm:
        executePrimaryKeyCheck(object_name, sourcelayer, rulename, sourceattr, sqlquery)

    elif "null" in rule_name_norm:
        executeNullCheck(object_name, sourcelayer, rulename, sourceattr, sqlquery)

    else:
        print(f"Unknown rule type: {rulename}")

# COMMAND ----------

# Read watermark
df_watermark = QueryFromDatabase("SELECT watermarkvalue FROM dqr.incremental_load_mappings WHERE tablename='dqr.dqresults'")
watermark_value = df_watermark.collect()[0][0]

# COMMAND ----------

# Read all check results
schema = StructType([
    StructField("objectname", StringType(), True),
    StructField("sourcelayer", StringType(), True),
    StructField("targetlayer", StringType(), True),
    StructField("rulename", StringType(), True),
    StructField("sourceresult", DecimalType(20,4), True),
    StructField("targetresult", DecimalType(20,4), True),
    StructField("rundatetime", TimestampType(), True)
])

df_check_results = (
    spark.read.format("csv")
    .option("header","true")
    .schema(schema)
    .option("recursiveFileLookup","true")
    .option("path", f"/Volumes/{catalog_name}/{dq_schema_name}/dqcheckresults/")
    .load()
)


# COMMAND ----------

df_check_results_final = df_check_results.filter(F.col("rundatetime") > F.lit(watermark_value))
display(df_check_results_final)

# COMMAND ----------

# Write results to SQL
WriteDataframeToDatabaseMode(df_check_results_final, "dqr.dqresults", "append")
display(QueryFromDatabase("SELECT TOP 100 * FROM dqr.dqresults ORDER BY rundatetime DESC"))


# COMMAND ----------

# Read final DQ results from SQL
df_results = QueryFromDatabase("SELECT TOP 100 * FROM dqr.dqresults ORDER BY rundatetime DESC")
display(df_results)

# COMMAND ----------

# Path to bad records
bad_records_path = "/Volumes/dbw_oncom_dev_001_7405615875359132/dataquality/dqcheckbadrecords/"

# Read all bad records
df_bad = (
    spark.read.format("csv")
    .option("header", "true")
    .option("recursiveFileLookup", "true")
    .load(bad_records_path)
)

display(df_bad)

# COMMAND ----------

# Read watermark
df_watermark = QueryFromDatabase(
    "SELECT * FROM dqr.incremental_load_mappings WHERE tablename='dqr.dqresults'"
)
display(df_watermark)
