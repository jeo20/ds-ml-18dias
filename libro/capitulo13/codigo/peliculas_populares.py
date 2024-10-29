from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def loadMovieNames():
    movieNames = {}
    with open("u.item",encoding = "ISO-8859-1") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

# Crear objeto SparkSession
spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

# Obtener nombres de películas
nameDict = loadMovieNames()

lines = spark.sparkContext.textFile("u.data")
movies = lines.map(lambda x: Row(movieID =int(x.split()[1])))

# Crear dataframe
movieDataset = spark.createDataFrame(movies)

topMovieIDs = movieDataset.groupBy("movieID").count().orderBy("count", ascending=False).cache()

#|movieID|count|
#+-------+-----+
#|     50|  584|
#|    258|  509|
#|    100|  508|

topMovieIDs.show()

top20_movies = topMovieIDs.take(20)

print("\n")
for result in top20_movies:
    print("%s: %d" % (nameDict[result[0]], result[1]))

spark.stop()
