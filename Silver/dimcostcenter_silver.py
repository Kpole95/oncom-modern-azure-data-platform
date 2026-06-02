# Databricks notebook source
# MAGIC %md
# MAGIC ###Run Shared Libraries

# COMMAND ----------

# MAGIC %run ../Misc/sharedlibraries

# COMMAND ----------

UpdatedDateTime = datetime.datetime.now()
Entity = "dimcostcenter"

# COMMAND ----------

# MAGIC %md
# MAGIC ###Read Bronze tables

# COMMAND ----------

costcenterDf = spark.table("bronze.costcenter")

# COMMAND ----------

costcenterDf.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Build Dimension/Fact table

# COMMAND ----------

dimcostcenterDf = costcenterDf.filter(costcenterDf.RecordId.isNotNull()
    ).select(
        costcenterDf.CostCenterNumber,
        F.when(costcenterDf.LastProcessedChange_DateTime.isNull(), F.lit("1900-01-01")).otherwise(costcenterDf.LastProcessedChange_DateTime).cast("timestamp").alias("LastProcessedChange_DateTime"),
        F.from_utc_timestamp(costcenterDf.DataLakeModified_DateTime,'CST').alias("DataLakeModified_DateTime"),
        costcenterDf.Vat,
        costcenterDf.RecordId.alias("CostCenterRecordId")
    ).withColumn("UpdatedDateTime", F.lit(UpdatedDateTime)
    ).withColumn("CostCenterHashKey", F.xxhash64("CostCenterRecordId")
    )

display(dimcostcenterDf)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Final dataframe

# COMMAND ----------

df_final = dimcostcenterDf

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write to Silver Schema

# COMMAND ----------

saveDeltaTableToCatalog(df_final,"silver",Entity)

# COMMAND ----------



# COMMAND ----------


