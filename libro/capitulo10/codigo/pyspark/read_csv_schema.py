from pyspark import SparkContext
from pyspark.sql import SparkSession,SQLContext, Row

### Create a Spark Session
spark = SparkSession.builder.master("local").appName("AppName").getOrCreate()
movies = spark.read.csv("movies.csv", header=True, inferSchema= True)
movies.printSchema()

