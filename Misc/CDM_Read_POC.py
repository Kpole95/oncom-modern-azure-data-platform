# Databricks notebook source
# MAGIC %run ./ADLS_oauth

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, LongType, TimestampType

# COMMAND ----------

partiesSchema = StructType([
    StructField("PartyId", LongType(), True),
    StructField("PartyName", StringType(), True),
    StructField("LastProcessedChange_DateTime", TimestampType(), True),
    StructField("DataLakeModified_DateTime", TimestampType(), True),
    StructField("PartyAddressCode", LongType(), True),
    StructField("EstablishedDate", TimestampType(), True),
    StructField("PartyEmailId", StringType(), True),
    StructField("PartyContactNumber", StringType(), True),
    StructField("RecordId", LongType(), True),
    StructField("TaxId", StringType(), True)
])

# COMMAND ----------

df = (spark.read.format("csv")
 .schema(partiesSchema)
 .option("header", "false")
 .option("path", "abfss://oaonoperationsdev@stoncomdev001.dfs.core.windows.net/oaon-sandbox.operations.dynamics.com/Tables/Purchase/Parties/")
 .load())
display(df)

# COMMAND ----------

df.printSchema()
