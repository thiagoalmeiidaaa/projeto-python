from delta.tables import *
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Delta Example") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Carregando a tabela
deltaTable = DeltaTable.forPath(spark, "../data/delta_vendas")

# INSERT
spark.sql("INSERT INTO delta.`../data/delta_vendas` VALUES (3, 'Carlos', 200, '2025-04-25')")

# UPDATE
deltaTable.updateExpr("cliente = 'Carlos'", {"valor": "250"})

# DELETE
deltaTable.delete("cliente = 'Carlos'")
