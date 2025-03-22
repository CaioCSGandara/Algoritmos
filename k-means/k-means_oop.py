import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, load_wine
from sklearn.decomposition import PCA


class KMeansAnalytic:

    def __init__(self, dataset):
        self.dataset = dataset
        self.reduced_data = None
        self.list_clusters = []
        self.list_inertias = []
        self.qtd_clusters_otima = 0
        self.xaxis = None
        self.yaxis = None
        self.target = None


    def k_means(self, qtd_clusters):
        return KMeans(qtd_clusters).fit(self.dataset.data)

    @staticmethod
    def inercia(kmeans):
        return kmeans.inertia_


    def run_kmeans_with_dif_knumbers(self):
        for i in range(1, 11):
            self.list_clusters.append(i)
            kmeans = self.k_means(i)
            inertia = self.inercia(kmeans)
            self.list_inertias.append(inertia)


    def plot_elbow_method(self):
        plt.plot(self.list_clusters, self.list_inertias)
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Inertia')
        plt.title('Elbow Method with inertia')
        plt.xticks(self.list_clusters)
        plt.grid()
        plt.show()


    def apply_pca(self):
        kmeans = KMeans(self.qtd_clusters_otima).fit(self.dataset.data)
        self.target = kmeans.predict(self.dataset.data)

        self.reduced_data = PCA(n_components=2).fit_transform(self.dataset.data)


    def plot_kmeans_clustering(self):
        fig = plt.figure(1, figsize=(10, 8))
        ax = fig.add_subplot()

        ax.scatter(
            self.reduced_data[:, 0],
            self.reduced_data[:, 1],
            c = self.target,
            s=40
        )

        plt.show()


if __name__ == "__main__":
    iris = load_iris()
    kma = KMeansAnalytic(iris)

    kma.run_kmeans_with_dif_knumbers()

    kma.plot_elbow_method()

    kma.qtd_clusters_otima = int(input("Qual o número de k ótimo apontado pelo elbow method?:  "))
    kma.apply_pca()
    kma.plot_kmeans_clustering()




