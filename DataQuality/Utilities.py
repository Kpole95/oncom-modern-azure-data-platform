# Databricks notebook source
from databricks.sdk.runtime import *

# COMMAND ----------

# Databricks notebook source

server_name = "jdbc:sqlserver://dataquality.database.windows.net:1433"
database_name = "sqldb-oncom-dq-dev"

jdbcurl = (
    server_name
    + ";databaseName="
    + database_name
    + ";encrypt=true;trustServerCertificate=false;"
    + "hostNameInCertificate=*.database.windows.net;loginTimeout=30;"
)

secret_scope = "kv-oncom-dev-scope"
sqlusername = dbutils.secrets.get(secret_scope, "sqlusername")
sqlpassword = dbutils.secrets.get(secret_scope, "sqlpassword")

# COMMAND ----------

# Read table function
def ReadTableFromDatabase(tablename: str):
    df = (
        spark.read.format("jdbc")
        .option("url", jdbcurl)
        .option("user", sqlusername)
        .option("password", sqlpassword)
        .option("dbtable", tablename)
        .load()
    )
    return df

# COMMAND ----------

# Read SQL query function
def QueryFromDatabase(sqlquery: str):
    df = (
        spark.read.format("jdbc")
        .option("url", jdbcurl)
        .option("user", sqlusername)
        .option("password", sqlpassword)
        .option("query", sqlquery)
        .load()
    )
    return df

# COMMAND ----------

def WriteDataframeToDatabase(dfName,Tablename):
    (dfName.write
    .format("jdbc")
    .option("url", jdbcurl) 
    .option("dbtable", Tablename)
    .option("user", sqlusername) 
    .option("password", sqlpassword) 
    .save()
        )

# COMMAND ----------

def WriteDataframeToDatabaseOverwrite(dfName,Tablename):
    (dfName.write.format("jdbc")
        .option("url",jdbcurl)
        .option("username",sqlusername)
        .option("password",sqlpassword)
        .mode("overwrite")
        .option("dbtable",Tablename).save()
        )

# COMMAND ----------

def WriteDataframeToDatabaseMode(dfName,Tablename,writemode):
    (dfName.write.format("jdbc")
        .option("url",jdbcurl)
        .option("username",sqlusername)
        .option("password",sqlpassword)
        .mode(writemode)
        .option("dbtable",Tablename).save()
        )
