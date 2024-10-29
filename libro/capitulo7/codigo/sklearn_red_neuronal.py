import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

iris=load_iris()
caracteristicas = iris.data
clases = iris.target
Xent, Xtest, yent, ytest= train_test_split(caracteristicas, clases)
red_neural = MLPClassifier(max_iter=15000, hidden_layer_sizes=(7))
red_neural.fit(Xent, yent)
red_neural.score(Xtest, ytest)
