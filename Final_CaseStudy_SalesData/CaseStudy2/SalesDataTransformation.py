{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "a0b3667d-7d26-4b39-b28a-c3a8025bc6d2",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql import SparkSession\n",
    "\n",
    "spark = SparkSession.builder \\\n",
    "    .appName(\"MyApp\") \\\n",
    "    .getOrCreate()\n",
    "\n",
    "# spark.conf.set(\"fs.azure.account.key.xyzretailstorage741.blob.core.windows.net\", \"GX8raMsS5CSD1TdyMlIoi89zRSQ3JS5RiF0eVHGd/SnQrTy9SbeiFdtINvYtAu/fwCS74MHMlZ9w+AStJwMXjQ==\")\n",
    "\n",
    "\n",
    "# df = spark.read.format(\"csv\").option(\"header\", \"true\").load(\"wasbs://source-data@xyzretailstorage741.blob.core.windows.net/sales_data.csv\")\n",
    "\n",
    "df = (spark.read\n",
    "  .format(\"delta\")\n",
    "  .option(\"mode\", \"PERMISSIVE\")\n",
    "  .load(\"https://xyzretailstorage741.blob.core.windows.net/source-data/sales_data.csv\")\n",
    ")\n",
    "# df = spark.read.format(\"csv\").load(\"https://xyzretailstorage741.blob.core.windows.net/source-data/sales_data.csv\")\n",
    "\n",
    "# Display DataFrame\n",
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "44a58348-4f8e-4ce2-9dfd-0c720b0c5e79",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import col, sum as _sum\n",
    "\n",
    "# Data Cleaning: Remove rows with null values\n",
    "df_cleaned = df.dropna()\n",
    "\n",
    "# Data Aggregation: Calculate total sales per product\n",
    "df_aggregated = df_cleaned.groupBy(\"Product line\").agg(_sum(\"Total\").alias(\"total_sales\"))\n",
    "\n",
    "# Write the transformed data back to Azure Blob Storage\n",
    "df_aggregated.write.format(\"csv\").option(\"header\", \"true\").mode(\"overwrite\").save(\"wasbs://transformed-data@xyzretailstorage741.blob.core.windows.net/transformed_sales_data.csv\")\n",
    "\n",
    "# Display the transformed DataFrame\n",
    "df_aggregated.show(truncate=False)"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "environmentMetadata": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "SalesDataTransformation",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
