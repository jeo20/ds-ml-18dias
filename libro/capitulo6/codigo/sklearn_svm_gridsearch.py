from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import numpy as np

iris = datasets.load_iris()
X, y = iris.data, iris.target
 
#Data sets de training y de test
X_entrenamiento, X_test, y_entrenamiento, y_test = train_test_split(X, y, random_state=1)

param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]

grid_search = GridSearchCV(SVC(),param_grid,cv=5,verbose=2)
grid_search.fit(X_entrenamiento,y_entrenamiento)
print(sorted(grid_search.cv_results_.keys()))
print(grid_search.best_params_,grid_search.best_score_  )
grid_search.score(X_test,y_test)
