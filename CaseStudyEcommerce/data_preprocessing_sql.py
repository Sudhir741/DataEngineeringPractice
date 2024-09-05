# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS ecommerce_db;
# MAGIC USE ecommerce_db;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE  transactions
# MAGIC USING CSV
# MAGIC OPTIONS (
# MAGIC   path '/FileStore/tables/processed_data.csv',
# MAGIC   header 'True',
# MAGIC   inferSchema 'True'
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM transactions LIMIT 10;
# MAGIC DESCRIBE transactions;
# MAGIC SELECT COUNT(*) - COUNT('Product ID') AS missing_values FROM transactions;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Transaction ID", COUNT(*) AS count
# MAGIC FROM transactions
# MAGIC GROUP BY "Transaction ID"
# MAGIC HAVING COUNT(*) > 1;
