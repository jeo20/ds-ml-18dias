from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *

sc = SparkContext("local[*]","My app")

sqlContext = SQLContext(sc)
lines = sc.textFile("data.txt")
parts = lines.map(lambda x:x.split(","))
data = parts.map(lambda x: Row(x[0], x[1].strip()))

schemaString="name age"

#fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]

fields = [StructField("name", StringType(), True),  StructField("age", StringType(), True)]

schema = StructType(fields)

schemaData = sqlContext.createDataFrame(data,schema)
schemaData.registerTempTable("DATA")
consulta = sqlContext.sql("SELECT * from DATA")
consulta.show()





