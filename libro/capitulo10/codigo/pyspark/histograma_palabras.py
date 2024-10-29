from pyspark import SparkContext
import re

sc = SparkContext("local[*]","My app")

rdd=sc.textFile("test.log")

words=rdd.flatMap(lambda linea:re.compile("\W").split(linea)).filter(lambda word:word !='').map(lambda word:word.lower())

histograma = words.map(lambda word:(word,1)).reduceByKey(lambda x,y:x+y)
print(histograma.collect())
for palabra in histograma.collect():
	print(str(palabra[0])+"-->",str(palabra[1]))


