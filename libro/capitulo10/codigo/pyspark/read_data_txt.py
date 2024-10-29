from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

sc = SparkContext("local[*]","My app")

sqlContext = SQLContext(sc)
lines = sc.textFile("data.txt")
parts = lines.map(lambda x:x.split(","))
data = parts.map(lambda x: Row(name=x[0], age=int(x[1])))
schemaData = sqlContext.createDataFrame(data)
schemaData.registerTempTable("DATA")
schemaData.printSchema()
schemaData.show()
consulta = sqlContext.sql("SELECT * from DATA")
consulta.show()
names = data.map(lambda x:"Name:"+x.name)
for name in names.collect():
   print(name)

ages = data.map(lambda x:"Age:"+str(x.age))
for age in ages.collect():
   print(age)




