from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

random_state = np.random.RandomState(42)
X = random_state.uniform(size=(30,1))
a = random_state.normal(scale=10)
b = random_state.normal()
y = np.dot(X,a).ravel()+b
y = y + random_state.normal(size=len(y))

# Definir el modelo de regresión
model = LinearRegression()

# Calcular la regresión
model.fit(X, y)

# Mostrar los resultados de la regresión
coef = model.coef_[0]
intercept = model.intercept_
print("coef=", coef, "intercept=", intercept)

y_predict= model.predict(X)

plt.plot(X[:,0],y,'x')
plt.plot(X[:,0],y_predict)

