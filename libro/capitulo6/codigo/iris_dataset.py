import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
 
iris = datasets.load_iris()
 
# sólo tomamos las 2 primeras features
X = iris.data[:, :2] 
Y = iris.target
 
# Pintamos los puntos de entrenamiento
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

