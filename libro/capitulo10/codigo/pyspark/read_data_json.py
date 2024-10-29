from pyspark import SparkContext

sc = SparkContext("local[*]","My app")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
dataframe = sqlContext.read.json("data.json")
dataframe.printSchema()
dataframe.show()

dataframe.select("name").show()
dataframe.select(dataframe['name'], dataframe['age']+1).show()
dataframe.filter(dataframe['age']>30).show()


dataframe.registerTempTable("DATA")
consulta=sqlContext.sql("SELECT * from DATA")



