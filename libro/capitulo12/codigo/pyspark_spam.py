from pyspark import SparkConf, SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.feature import HashingTF

#cargar SparkContext
conf = SparkConf().setAppName("spam")
sc = SparkContext(conf=conf)
    
spam = sc.textFile("spam.txt")
no_spam = sc.textFile("no_spam.txt")

# Creo un objeto HashingTF para extraer características a partir de un mensaje de email
Hashing_TF = HashingTF(numFeatures = 100)

# Cada email se divide en palabras y cada palabra se convierte en una feature que nos permitirá
# posteriormente caracterizar si un email es spam o no
spam_features = spam.map(lambda email: Hashing_TF.transform(email.split(" ")))
no_spam_features = no_spam.map(lambda email: Hashing_TF.transform(email.split(" ")))

print("Spam features:")
print(spam_features.collect())

print("No Spam features:")
print(no_spam_features.collect())

# Creamos datasets de etiquetas para casos de spam y no spam
spam_ejemplos = spam_features.map(lambda features: LabeledPoint(1, features))
no_spam_ejemplos = no_spam_features.map(lambda features: LabeledPoint(0, features))

# datos de entrenamiento
datos_entrenamiento = spam_ejemplos.union(no_spam_ejemplos)

# Cacheamos los datos para aplicar posteriormente un modelo iterativo
datos_entrenamiento.cache()

# Ejecutamos nuestro modelo de regresión logística sobre los datos de entrenamiento
modelo = LogisticRegressionWithSGD.train(datos_entrenamiento)

test_spam = Hashing_TF.transform("GET this product by sending money to account".split(" "))
test_spam2 = Hashing_TF.transform("If you think you have a virus check this".split(" "))
test_no_spam = Hashing_TF.transform("I am studying python because I want be a python developer for web applications".split(" "))

# Prediccción para nuevos mensajes de email con el modelo creado
print("Prediction for test_spam: %g" % modelo.predict(test_spam))
print("Prediction for test_spam2: %g" % modelo.predict(test_spam2))
print("Prediction for test_no_spam: %g" % modelo.predict(test_no_spam))
