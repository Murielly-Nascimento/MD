from sklearn.cluster import k_means, AgglomerativeClustering
from sklearn.metrics import silhouette_score, jaccard_score
import pandas
import numpy as np
from sklearn import metrics

def purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    # return purity
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

# carregando blobs.csv sem a coluna 'label'
dados = pandas.read_csv('seeds.csv', usecols=[0,1,2,3,4,5,6],index_col=False)
dados = dados.values

# Executando o algoritmo k-means.
#centroides, rotulos, sse = k_means(dados,n_clusters=4,init='random',n_init=100)

#clustering_model = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='single')
clustering_model = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='complete')
clustering_model.fit(dados)
rotulos = clustering_model.labels_

# Calculando a largura de silhueta.
# O primeiro parametro eh o conjunto de dados estudado.
# O segundo engloba os rotulos encontrados por um algoritmo.
# O parametro 'metric' indica a medida de distancia
# utilizada. No caso do algoritmo k-means, sera informado
# 'sqeuclidean' que eh a distancia euclidiana ao
# quadrado.

classe = pandas.read_csv('seeds.csv', usecols=[7],index_col=False)
classe = classe.values
classe = classe.ravel()

s = silhouette_score(dados, rotulos, metric='sqeuclidean')
j = jaccard_score(classe, rotulos, average='micro')
p = purity_score(classe, rotulos)

print("Largura da silhueta ", s)
print("Grau de Pureza ", p)
print("Coeficiente de Jaccard ", j)






	