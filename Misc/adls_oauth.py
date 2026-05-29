# Databricks notebook source
# MAGIC %md
# MAGIC ## Purpose:
# MAGIC
# MAGIC Authenticate Databricks Spark to ADLS Gen2 using service principal credentials from Databricks secret scope.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Define secret scope and storage account variables
# MAGIC
# MAGIC This notebook configures Spark OAuth access to ADLS Gen2.
# MAGIC
# MAGIC Secrets are read from the Databricks secret scope. No secret values are hardcoded.

# COMMAND ----------

# Secret scope and secret key names used to read service principal credentials.

secret_scope = "kv-oncom-dev-scope"             # Databricks secret scope linked to Key Vault
client_secret_key = "client-secret"             # secret key containing app/client secret
app_id_key = "app-id"                           #secret key containing app/client ID
tenant_id_key = "tenant-id"                     #secret key containing Azure tenant ID

# ADLS Gen2 storage account name.
storage_account = "stoncomdev001"               # ADLS Gen2 storage account

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read service principal secrets
# MAGIC
# MAGIC Read the client secret, application ID, and tenant ID from Databricks secrets.

# COMMAND ----------

# Read service principal credentials from Databricks secret scope.
# These values are needed for OAuth authentication to ADLS Gen2.

service_credential = dbutils.secrets.get(scope=secret_scope, key=client_secret_key) # client secret
appid = dbutils.secrets.get(scope=secret_scope, key=app_id_key) # app registration / service principal client ID
tenantid = dbutils.secrets.get(scope=secret_scope, key=tenant_id_key)   # Azure Active Directory tenant ID

# COMMAND ----------

# MAGIC %md
# MAGIC ### Validate tenant ID format
# MAGIC
# MAGIC The tenant ID must be only the tenant GUID.
# MAGIC
# MAGIC It must not contain a URL, `microsoftonline`, `/oauth2/token`, or slashes.

# COMMAND ----------

# Safe validation of tenant ID format.

print("tenantid length:", len(tenantid))
print("tenantid starts with https:", tenantid.startswith("https"))
print("tenantid contains microsoftonline:", "microsoftonline" in tenantid)
print("tenantid contains slash:", "/" in tenantid)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configure Spark OAuth access to ADLS Gen2
# MAGIC
# MAGIC Configure Spark to use service principal OAuth authentication for the ADLS Gen2 storage account.

# COMMAND ----------

# Configure Spark OAuth access for ADLS Gen2.

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

print("ADLS OAuth configuration completed.")


# Use OAuth authentication for stoncomdev001.dfs.core.windows.net
# Use the service principal client ID
# Use the service principal client secret
# Get token from Azure AD tenant endpoint

# COMMAND ----------

# MAGIC %md
# MAGIC ### Test ADLS container access
# MAGIC
# MAGIC List the ADLS container root to confirm authentication and storage access are working.

# COMMAND ----------

# Test whether Databricks can list the ADLS container root.

display(dbutils.fs.ls("abfss://oaonoperationsdev@stoncomdev001.dfs.core.windows.net/"))

