from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import regexp_extract
from pyspark.sql.types import *
from pyspark.sql import SQLContext
from pyspark.sql import functions as F

conf = (SparkConf().setMaster("local").setAppName("Recomendador").set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

ratings_df_schema = StructType(
  [StructField('userId', IntegerType()),
   StructField('movieId', IntegerType()),
   StructField('rating', DoubleType())]
)
movies_df_schema = StructType(
  [StructField('ID', IntegerType()),
   StructField('title', StringType())]
)

raw_ratings_df = sqlContext.read.format('com.databricks.spark.csv').options(header=True, inferSchema=False).schema(ratings_df_schema).load('ratings.csv')
ratings_df = raw_ratings_df.drop('Timestamp')

ratings_df.show(5)


raw_movies_df = sqlContext.read.format('com.databricks.spark.csv').options(header=True, inferSchema=False).schema(movies_df_schema).load('movies.csv')
movies_df = raw_movies_df.drop('Genres').withColumnRenamed('movieId', 'ID')

movies_df.show(5, truncate=False)

movie_ids_with_avg_ratings_df = ratings_df.groupBy('movieId').agg(F.count(ratings_df.rating).alias("count"), F.avg(ratings_df.rating).alias("average"))
movie_ids_with_avg_ratings_df.show(5, truncate=False)

movie_names_df = movie_ids_with_avg_ratings_df.join(movies_df,movie_ids_with_avg_ratings_df["movieId"]==movies_df["Id"])
movie_names_with_avg_ratings_df = movie_names_df.drop("Id")

movie_names_with_avg_ratings_df.show(5, truncate=False)

movies_with_100_ratings_or_more = movie_names_with_avg_ratings_df.where(movie_names_with_avg_ratings_df["count"]>=100)
print('20 Películas con mayores puntuaciones:')
movies_with_100_ratings_or_more.show(20, truncate=False)

# Reservaremos el 60 % para entrenamiento, el 20 % de nuestros datos para validación y dejaremos el 20 % para pruebas
(split_60_df, split_a_20_df, split_b_20_df) = ratings_df.randomSplit([0.6,0.2,0.2])

training_df = split_60_df.cache()
validation_df = split_a_20_df.cache()
test_df = split_b_20_df.cache()

print('Entrenamiento: {0}, Validacion: {1}, Test: {2}\n'.format(training_df.count(), validation_df.count(), test_df.count()))

training_df.show(3)
validation_df.show(3)
test_df.show(3)

from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

als = ALS()
als.setMaxIter(5).setRegParam(0.1).setUserCol("userId").setItemCol("movieId").setRatingCol("rating")
reg_eval = RegressionEvaluator(predictionCol="prediction", labelCol="rating", metricName="rmse")

tolerance = 0.03
ranks = [4, 8, 12]
errors = [0, 0, 0]
models = [0, 0, 0]
err = 0
min_error = float('inf')
best_rank = -1
for rank in ranks:
  als.setRank(rank)
  
  # Crear el modelo a partir de los datos de entrenamiento
  model = als.fit(training_df)
  
  # Realizar la predicción sobre los datos de validacion
  predict_df = model.transform(validation_df)

  # Eliminar valores nulos de la prediccion
  predicted_ratings_df = predict_df.filter(predict_df.prediction != float('nan'))

  # Ejecutar el evaluador que permite obtener el error cometido
  error = reg_eval.evaluate(predicted_ratings_df)
  errors[err] = error
  models[err] = model
  print('El error cometido para el rank %s es %s' % (rank, error))
  if error < min_error:
    min_error = error
    best_rank = err
  err += 1

als.setRank(ranks[best_rank])
print('El mejor modelo es entrenado con el rank %s' % ranks[best_rank])
my_model = models[best_rank]


from pyspark.sql import Row
my_user_id = 0

my_rated_movies = [
      (my_user_id, 1193, 3.5),
      (my_user_id, 914, 2.5),
      (my_user_id, 2355, 4.2),
      (my_user_id, 1287, 3.7),
      (my_user_id, 594, 3.1),
      (my_user_id, 595, 2.6),
      (my_user_id, 2398, 1.7),
      (my_user_id, 1035, 4.0),
      (my_user_id, 2687, 5.0),
      (my_user_id, 3105, 4.7),
      (my_user_id, 1270, 2.5)
]

my_ratings_df = sqlContext.createDataFrame(my_rated_movies, ['userId','movieId','rating'])
my_ratings_df.show(10)

training_with_my_ratings_df = training_df.unionAll(my_ratings_df)

als.setPredictionCol("prediction").setMaxIter(5).setRegParam(0.1).setUserCol("userId").setItemCol("movieId").setRatingCol("rating").setRank(ranks[best_rank])
my_ratings_model = als.fit(training_with_my_ratings_df)

my_rated_movie_ids = [x[1] for x in my_rated_movies]
not_rated_df = movies_df.filter(~ movies_df["ID"].isin(my_rated_movie_ids))
my_unrated_movies_df = not_rated_df.selectExpr("ID as movieId").withColumn('userId', F.lit(my_user_id))
raw_predicted_ratings_df = my_ratings_model.transform(my_unrated_movies_df)
predicted_ratings_df = raw_predicted_ratings_df.filter(raw_predicted_ratings_df['prediction'] != float('nan'))


predicted_with_counts_df = predicted_ratings_df.join(movie_names_with_avg_ratings_df,movie_names_with_avg_ratings_df["movieId"]==predicted_ratings_df["movieId"])
predicted_highest_rated_movies_df = predicted_with_counts_df.filter(predicted_with_counts_df["count"]>100).sort("prediction",ascending=False)

print ('Películas mejor calificadas con más de 100 reseñas:')
predicted_highest_rated_movies_df.show(20)



