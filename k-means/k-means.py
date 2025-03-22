import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

from sklearn.decomposition import PCA

iris = load_iris()


qtd_clusters = 3
legenda = [f"Grupo {i+1}" for i in range(qtd_clusters)]

kmeans = KMeans(qtd_clusters).fit(iris.data)

inercia = kmeans.inercia_

target = kmeans.predict(iris.data)

fig = plt.figure(1, figsize=(10, 8))
ax = fig.add_subplot()

iris_reduced = PCA(n_components=2).fit_transform(iris.data)
scatter = ax.scatter(
    iris_reduced[:, 0],
    iris_reduced[:, 1],
    c=target,
    s=40,
)

ax.set(
    title="Classificação morfológica de flores por comprimento e largura de sépalas e pétalas",
)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])


legend1 = ax.legend(
    scatter.legend_elements()[0],
    legenda,
    loc="upper right",
    title="Classes",
)
ax.add_artist(legend1)

plt.show()