import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn import datasets
 
# Importamos el dataset
iris = datasets.load_iris()
 
# Tomamos el ancho y longitud del pétalo
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
 
 
#Definimos un número de vecinos relativamente grande, k = 15
n_neighbors = 15
 
# Creamos los colormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

 
for weights in ['uniform', 'distance']:
   # Creamos una instancia de Neighbors Classifier y hacemos un fit a partir de los
   # datos.
   # Los pesos (weights) determinarán en qué proporción participa cada punto en la
   # asignación del espacio. De manera uniforme o proporcional a la distancia.
   clf = RadiusNeighborsClassifier(3.0, weights='distance')
   clf.fit(X, y)
 
   # Creamos una gráfica con las zonas asignadas a cada categoría según el modelo
   # k-nearest neighborgs. Para ello empleamos el meshgrid de Numpy.
   # A cada punto del grid o malla le asignamos una categoría según el modelo knn.
   # La función c_() de Numpy, concatena columnas.
   h = .02
   x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
   y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
   xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
   np.arange(y_min, y_max, h))
   Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
 
   # Ponemos el resultado en un gráfico.
   Z = Z.reshape(xx.shape)
   plt.figure()
   plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
 
   # Representamos también los datos de entrenamiento.
   plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
   plt.xlim(xx.min(), xx.max())
   plt.ylim(yy.min(), yy.max())
   plt.title("3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights))
   plt.xlabel('Petal Width')
   plt.ylabel('Petal Length')
   plt.savefig('iris-knn-{}'.format(weights))
