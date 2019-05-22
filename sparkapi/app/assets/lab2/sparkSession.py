from pyspark.sql import SparkSession

SPARK_SESSION = SparkSession.builder.appName('classifier').getOrCreate()