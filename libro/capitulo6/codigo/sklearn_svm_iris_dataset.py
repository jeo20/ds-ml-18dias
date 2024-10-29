from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import numpy as np

iris = datasets.load_iris()
X, y = iris.data, iris.target
 
#Data sets de training y de test
X_entrenamiento, X_test, y_entrenamiento, y_test = train_test_split(X, y, random_state=1)
classifier = SVC(kernel='rbf', C=1.0, gamma=0.7, random_state=101)
classifier.fit(X_entrenamiento,y_entrenamiento)
classifier.predict(X_entrenamiento)
print(classifier.score(X_entrenamiento,y_entrenamiento))
print(classifier.score(X_test,y_test))

scores = cross_val_score(classifier, X, y, cv=20, scoring='accuracy')
print('Accuracy: %0.3f' % np.mean(scores))
