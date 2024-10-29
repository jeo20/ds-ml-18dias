val textFile = spark.sparkContext.textFile("bin/pyspark.cmd")
val counts = textFile.flatMap(line => line.split(" "))
.map(word => (word, 1))
.reduceByKey(_ + _)
counts.collect.foreach(println _)

