import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn import metrics
from sklearn.metrics.cluster import silhouette_score
iris = datasets.load_iris()
datos = iris.data
etiquetas = iris.target
scores=[]
for n_clusters in range(2,10):
  k_means = KMeans(n_clusters=n_clusters, max_iter=2000).fit(datos)
  scores.append(silhouette_score(datos,k_means.labels_))

plt.plot(range(2,10),scores)
