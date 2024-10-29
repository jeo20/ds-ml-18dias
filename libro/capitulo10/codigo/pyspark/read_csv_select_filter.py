from pyspark.sql import SparkSession

### Create a Spark Session
spark = SparkSession.builder.master("local").appName("AppName").getOrCreate()

movies = spark.read.csv("movies.csv", header=True, mode="DROPMALFORMED")

movies.select('movieId','genres').show(5)

movies.filter(movies['movieId']>10).show(5)
