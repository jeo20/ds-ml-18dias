from pyspark.sql import SparkSession

### Create a Spark Session
spark = SparkSession.builder.master("local").appName("AppName").getOrCreate()

movies = spark.read.csv("movies.csv", header=True, mode="DROPMALFORMED")

movies.createOrReplaceTempView("MOVIES")
datos = spark.sql("SELECT * FROM MOVIES where movieId>10 and movieId<20")
datos.show()

