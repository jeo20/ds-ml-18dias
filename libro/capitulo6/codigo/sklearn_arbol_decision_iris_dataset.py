from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
 
# Cargamos dataset
iris = load_iris()
 
#Dividimos entre entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, stratify=iris.target, random_state=42)
 
#Creamos el modelo
model = DecisionTreeClassifier(random_state=0)
 
#Entrenamos los datos
model.fit(X_train, y_train)
 
#Obtenemos rendimiento sobre datos de entrenamiento y sobre datos de test
print("Accuracy on training set: {:.3f}".format(model.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(model.score(X_test, y_test)))

def plot_feature_importances_iris(model):
    n_features = iris.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), iris.feature_names)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
 
plot_feature_importances_iris(model)

#Dibujar el árbol entrenado
from sklearn import tree
fig, ax = plt.subplots(figsize=(10, 10)) #Tamaño del gráfico
tree.plot_tree(model, fontsize = 10)
