from sklearn.model_selection import train_test_split
from sklearn import datasets
 
iris_dataset = datasets.load_iris()

X_train, X_test, y_train, y_test =
train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

print('X_train',X_train)
print('X_test',X_test)
print('y_train',y_train)
print('y_test',y_test)



