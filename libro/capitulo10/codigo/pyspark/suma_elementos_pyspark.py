from pyspark import SparkConf, SparkContext

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)

rdd = sc.parallelize([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
print(rdd.collect()) 

cuadrado = rdd.map(lambda x: x*2)
suma = cuadrado.reduce(lambda x,y: x+y)
print("La suma de los elementos es: " + str(suma))




