import numpy as np
import matplotlib.pyplot as plt
random_state = np.random.RandomState(42)
X = random_state.uniform(size=(30,1))
a = random_state.normal(scale=10)
b = random_state.normal()
y = np.dot(X,a).ravel()+b
y= y+ random_state.normal(size=len(y))
plt.plot(X[:,0],y,'x')
