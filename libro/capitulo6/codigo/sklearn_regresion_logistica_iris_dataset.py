import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
 
#importar iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
 
#Entrenemos los datos con  LogisticRegression
model = linear_model.LogisticRegression(C=10000) # C = 1/alpha
model.fit(X, Y)
 
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
 
h = .02 
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
 
#Pintar el gráfico
 
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()
