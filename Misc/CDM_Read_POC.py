# Databricks notebook source
# MAGIC %md
# MAGIC ### Run ADLS OAuth setup
# MAGIC
# MAGIC Run the ADLS OAuth notebook so Spark can access the storage account.

# COMMAND ----------

# %run ./ADLS_oauth

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read raw CSV source folder
# MAGIC
# MAGIC Read the `Parties` CSV folder directly from ADLS.
# MAGIC
# MAGIC The CSV files do not contain headers, so Spark initially returns generic column names such as `_c0`, `_c1`, and `_c2`.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Service Principal Credentials
# MAGIC
# MAGIC This cell reads credentials again for the CDM connector test.
# MAGIC
# MAGIC This follows the instructor's notebook style.

# COMMAND ----------

# # Read credentials from secret scope.

# service_credential = dbutils.secrets.get(scope="kv-oncom-dev-scope",key="client-secret")
# appid = dbutils.secrets.get(scope="kv-oncom-dev-scope",key="app-id")
# tenantid = dbutils.secrets.get(scope="kv-oncom-dev-scope",key="tenant-id")

# COMMAND ----------

# MAGIC %md
# MAGIC ### StructType Fallback Test For Parties
# MAGIC
# MAGIC This cell manually defines the schema for `Parties` based on `Parties.cdm.json`.
# MAGIC
# MAGIC This proves that we can still read CDM-style data without the CDM connector.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Define Parties Schema
# MAGIC
# MAGIC This schema was verified from `Parties.cdm.json`.
# MAGIC
# MAGIC The CSV files are headerless, so the column order in this schema must match the column order in the source CSV.

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, LongType, TimestampType

# Define schema for the Parties entity.
# This schema is based on Parties.cdm.json.

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

# MAGIC %md
# MAGIC ### Read Parties CSV With StructType Schema
# MAGIC
# MAGIC This reads the headerless CSV folder using the manually defined schema.
# MAGIC
# MAGIC This produces the same useful result that the CDM connector was supposed to produce.

# COMMAND ----------

# Read Parties CSV files using the verified StructType schema.

dfParties = (spark.read.format("csv")
 .schema(partiesSchema)
 .option("header", "false")
 .option("path", "abfss://oaonoperationsdev@stoncomdev001.dfs.core.windows.net/oaon-sandbox.operations.dynamics.com/Tables/Purchase/Parties/")
 .load())

display(dfParties)

# Verify Parties Schema
#This verifies that the DataFrame has the expected column names and Spark data types.

df.printSchema()
