from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

boston = datasets.load_boston()
lr = LinearRegression(normalize=True)
lr.fit(boston.data, boston.target)
for (feature, coef) in zip(boston.feature_names, lr.coef_):
	print('{:>7}: {: 9.5f}'.format(feature, coef))

precio_estimado = lr.predict(boston.data)

boston_df = pd.DataFrame({'precio real':boston.target,'precio estimado':precio_estimado})
boston_df['error'] = abs(boston_df['precio real']-boston_df['precio estimado'])
print(boston_df)

X = boston.data
y = boston.target

X_entrenamiento, X_test, y_entrenamiento, y_test=train_test_split(X, y)

len(X_entrenamiento)
len(X_test)
len(y_entrenamiento)
len(y_test)

print('X_entrenamiento:',X_entrenamiento)
print('X_test:',X_test)
print('y_entrenamiento:',y_entrenamiento)
print('y_test:',y_test)
lr = LinearRegression(normalize=True)
lr.fit(X_entrenamiento, y_entrenamiento)

precio_estimado = lr.predict(X_test)
print('precio_estimado:',precio_estimado)

from sklearn.metrics import r2_score

r2_score(y_test, precio_estimado)
