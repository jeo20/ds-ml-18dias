import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
 
from sklearn.datasets.samples_generator import make_blobs
centers = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
X, y = make_blobs(n_samples=1000, centers=centers, cluster_std=0.5, random_state=101)
plt.scatter(X[:,0], X[:,1], c=y, edgecolors='none', alpha=0.9)
plt.show()

from sklearn.cluster import KMeans

for n_iter in range(1, 5):
  cls = KMeans(n_clusters=4, max_iter=n_iter, n_init=1, init='random', random_state=101)
  cls.fit(X)
 
  plt.subplot(2, 2, n_iter)
  h=0.02
  xx, yy = np.meshgrid(np.arange(-3, 3, h), np.arange(-3, 3, h))
  Z = cls.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
  plt.imshow(Z, interpolation='nearest', cmap=plt.cm.Accent, extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto', origin='lower')
  plt.scatter(X[:,0], X[:,1], c=cls.labels_, edgecolors='none', alpha=0.7)
  plt.scatter(cls.cluster_centers_[:,0], cls.cluster_centers_[:,1], marker='x', color='r', s=100, linewidths=4)
  plt.title("iter=%s, distortion=%s" %(n_iter, int(cls.inertia_)))
  plt.show()

