import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

# carico file necessario e faccio dei controlli
dt = pd.read_csv('20 Agosto\\Mall_Customers.csv')
print(dt.isna().sum().sum()) #controlla se ci sono nan, non ce ne sono
print(dt.describe())
print(dt)


### 1: clustering su campi Annual Income e Spending Score e interèretazione gruppi

# caratteristiche che devo usare per il clustering
X = dt[['Annual Income (k$)', 'Spending Score (1-100)']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# clustering
kmeans = KMeans(n_clusters=5, random_state=0)
labels = kmeans.fit_predict(X_scaled)

# aggiungo etichette a dataset
dt['Cluster'] = labels



### 2: visualizza grafico 2D

plt.figure(figsize=(6,6))
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=labels, cmap='viridis')
centroids_original = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids_original[:, 0], centroids_original[:, 1], c='red', marker='X', s=100, label='Centroidi')
plt.title('Cluster trovati con k-Means')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()



### 3: Identificare cluster che rappredenta clienti ad alto potenziale
# calcolo i centroidi e poi sommo reddito e spesa, il valore più alto è quello che ha entrambi i valori più alti
centroids = kmeans.cluster_centers_
high_potential = ((centroids[:, 0] + centroids[:, 1]).argmax())
print('Cluster ad alto potenziale:', high_potential)



### 4: Distanza media dei punti dal centroide del proprio cluster
distances = []
for c in range(kmeans.n_clusters):
    points = X[dt['Cluster'] == c].values
    centroid = centroids[c].reshape(1, -1)
    dists = euclidean_distances(points, centroid)
    distances.append(dists.mean())

print('Distanza euclidea media per cluster:', distances)