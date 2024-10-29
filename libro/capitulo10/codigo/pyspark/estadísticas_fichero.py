from pyspark import SparkContext

sc = SparkContext("local[*]","My app")

rdd=sc.textFile("README.md")

def estadisticas(line):
   return [("caracteres", len(line)), ("palabras", len(line.split())), ("lineas", 1)]
 
print (rdd.flatMap(estadisticas).reduceByKey(lambda a,b: a+b).collectAsMap())



