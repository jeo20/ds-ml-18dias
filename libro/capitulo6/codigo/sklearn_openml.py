from sklearn.datasets import fetch_openml
 
mnist = fetch_openml('mnist_784')
print(mnist.data) # (70000, 784)
print(mnist.target.shape) # (70000,)
np.unique(mnist.target) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

