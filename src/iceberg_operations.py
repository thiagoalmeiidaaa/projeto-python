from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Iceberg Example") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .getOrCreate()

# INSERT
spark.sql("INSERT INTO default.produtos VALUES (4, 'Teclado', 120.0)")

# UPDATE
spark.sql("UPDATE default.produtos SET valor = 135.0 WHERE id = 4")

# DELETE
spark.sql("DELETE FROM default.produtos WHERE id = 4")
