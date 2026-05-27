# Databricks notebook source
# Check available secret scopes
dbutils.secrets.listScopes()

# COMMAND ----------

# Databricks notebook source

# Replace with your values
secret_scope = "kv-oncom-dev-scope"
client_secret_key = "client-secret"
app_id_key = "app-id"
tenant_id_key = "tenant-id"

storage_account = "stoncomdev001"

# COMMAND ----------

# Read secrets from Databricks secret scope
service_credential = dbutils.secrets.get(
    scope=secret_scope,
    key=client_secret_key
)

appid = dbutils.secrets.get(
    scope=secret_scope,
    key=app_id_key
)

tenantid = dbutils.secrets.get(
    scope=secret_scope,
    key=tenant_id_key
)

# COMMAND ----------

# Configure Spark OAuth access to ADLS Gen2
spark.conf.set(
    f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net",
    "OAuth"
)

spark.conf.set(
    f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net",
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net",
    appid
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net",
    service_credential
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net",
    f"https://login.microsoftonline.com/{tenantid}/oauth2/token"
)

# COMMAND ----------

print("ADLS OAuth configuration completed.")

# COMMAND ----------

display(dbutils.fs.ls("abfss://oaonoperationsdev@stoncomdev001.dfs.core.windows.net/oaon-sandbox.operations.dynamics.com/Tables/Purchase/Parties/"))

