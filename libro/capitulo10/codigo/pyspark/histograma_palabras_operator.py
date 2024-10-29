from pyspark import SparkContext
from operator import add

sc = SparkContext("local[*]","My app")

rdd = sc.textFile("README.md") # Create RDD

def tokenize(text):
  return text.split()

histograma_palabras = rdd.flatMap(tokenize)
histograma_palabras = histograma_palabras.map(lambda x: (x,1)).reduceByKey(add).collectAsMap()
print(histograma_palabras)



