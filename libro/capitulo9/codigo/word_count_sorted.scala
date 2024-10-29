val textFile = spark.sparkContext.textFile("bin/pyspark.cmd")
val counts = textFile.flatMap(line => line.split(" "))
.map(word => (word, 1))
.reduceByKey(_ + _)
.map(item => item.swap)
.sortByKey(false)
.take(10)
counts.foreach(println _)

