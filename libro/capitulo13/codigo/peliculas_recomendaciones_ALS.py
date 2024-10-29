from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import ALS, Rating

def loadMovieNames():
    movieNames = {}
    with open("u.item", encoding='ascii', errors="ignore") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

conf = SparkConf().setMaster("local[*]").setAppName("MovieRecommendationsALS")
sc = SparkContext(conf = conf)

# Obtener nombres de películas
nameDict = loadMovieNames()

data = sc.textFile("u.data")

ratings = data.map(lambda l: l.split()).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2]))).cache()

# Construir el modelo de recomendacion usando ALS(Alternating Least Squares)
rank = 10
numIterations = 6
model = ALS.train(ratings, rank, numIterations)

userID =int(input("Introduce identificador de usuario:"))

print("\nPuntuaciones para el usuario ID " + str(userID) + ":")
userRatings = ratings.filter(lambda l: l[0] == userID)
for rating in userRatings.collect():
    print (nameDict[int(rating[1])] + ": " + str(rating[2]))

print("\nTop 20 recomendaciones para el usuario ID " + str(userID) + ":")
recommendations = model.recommendProducts(userID, 20)
for recommendation in recommendations:
    print (nameDict[int(recommendation[1])] + " score " + str(recommendation[2]))
