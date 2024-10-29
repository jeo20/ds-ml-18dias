from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
 
# generar datos en 2 dimensiones
X, y = make_blobs(random_state=1)
 
# construir el modelo de clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print("Etiquetas del Cluster:\n{}".format(kmeans.labels_))
