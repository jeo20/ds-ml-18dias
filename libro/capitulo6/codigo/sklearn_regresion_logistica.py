import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

X = np.array([[16,2], [3,1], [2,7], [13,4], [3,4], [12,5], [15,6], [4,6]])
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.show()

Y = [1, 0, 0, 1, 0, 1, 1, 0]

clase0 = np.array([X[i] for i in range(len(X)) if Y[i]==0])
clase1 = np.array([X[i] for i in range(len(X)) if Y[i]==1])

clasificador = linear_model.LogisticRegression(solver='lbfgs', C=100)
clasificador.fit(X, Y)

prediccion = clasificador.predict(X)
print(prediccion)

print(clasificador.score(X,Y))

Xn = np.array([[6,4], [20,7], [4,17]])
Yn = clasificador.predict(Xn)
print(Yn)








