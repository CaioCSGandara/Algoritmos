import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

matriz = np.random.randint(0, 2501, (50, 50))

matriz_reduced = PCA(n_components=2).fit_transform(matriz)

fig = plt.figure(1, figsize=(10,8))
ax = fig.add_subplot()

scatter = ax.scatter(
    matriz_reduced[:,0],
    matriz_reduced[:,1],
    s=40
)

plt.show()
