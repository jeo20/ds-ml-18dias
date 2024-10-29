# Definir las librerías a importar
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from time import time

# Generación de un dataset de 2 dimensiones X e Y
X, Y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=1)

start_time = time()

# Definir el modelo de regresión
model = LogisticRegression()

# Calcular la regresión
model.fit(X, Y)

prediccion = model.predict(X)
print(prediccion)

print(model.score(X,Y))
