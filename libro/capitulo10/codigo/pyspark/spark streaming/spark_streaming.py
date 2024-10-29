from pyspark import SparkContext
from pyspark.streaming import StreamingContext

spark_context = SparkContext(appName="Spark Streaming", master="local[*]")
streaming_context = StreamingContext(spark_context, 5)

lineas = streaming_context.socketTextStream("localhost", 9998)

histograma_palabras = lineas.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

histograma_palabras.pprint()
streaming_context.start()
streaming_context.awaitTermination()





