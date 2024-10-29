import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model, datasets, metrics
from sklearn.model_selection import cross_val_score 
 
#importar iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
 
#Definimos el modelo LogisticRegression
model = linear_model.LogisticRegression(C=10000)
 
#Dividimos en dataset
x_train, x_test, y_train, y_test = train_test_split(X, Y)
 
#Entrenemos los datos con  el modelo
model.fit(x_train, y_train)
 
#Realizamos una prediccion
y_pred = model.predict(x_test)
 
#Obtenemos rendimiento
print("Accuracy: %2f" % metrics.accuracy_score(y_test, y_pred))
print("Precision: %2f" % metrics.precision_score(y_test, y_pred,average="macro"))
print("F1: %2f" % metrics.f1_score(y_test, y_pred, average="macro"))
