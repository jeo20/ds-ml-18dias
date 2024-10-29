import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

dataset = spark.read.csv('BostonHousing.csv',inferSchema=True, header =True)
dataset.printSchema()

assembler = VectorAssembler(inputCols=['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat'], outputCol = 'Propiedades')
output = assembler.transform(dataset)
data = output.select("Propiedades","medv")
data.show()

train_data, test_data = data.randomSplit([0.8,0.2])
regressor_lineal = LinearRegression(featuresCol = 'Propiedades', labelCol = 'medv')
regressor_model = regressor_lineal.fit(train_data)
prediction = regressor_model.evaluate(test_data)
prediction.predictions.show()

coefficient = regressor_model.coefficients
intercept = regressor_model.intercept
print ("The coefficient of the model is:% a"% coefficient)
print ("The intercept of the model is:% f"% intercept)

from pyspark.ml.evaluation import RegressionEvaluator
eval = RegressionEvaluator(labelCol="medv", predictionCol="prediction", metricName="rmse")
rmse = eval.evaluate(prediction.predictions)
print("RMSE: %.3f" % rmse)
mse = eval.evaluate(prediction.predictions, {eval.metricName: "mse"})
print("MSE: %.3f" % mse)
mae = eval.evaluate(prediction.predictions, {eval.metricName: "mae"})
print("MAE: %.3f" % mae)
r2 = eval.evaluate(prediction.predictions, {eval.metricName: "r2"})
print("r2: %.3f" %r2)

