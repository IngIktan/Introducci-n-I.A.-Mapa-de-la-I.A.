# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa un Mapa Autoorganizado de Kohonen (SOM) en Python utilizando MiniSom.

from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Creamos un conjunto de datos de ejemplo
data = np.random.rand(100, 2)  # 100 puntos en 2 dimensiones

# Definimos el tamaño del SOM
som_size = (10, 10)  # Un SOM de 10x10 neuronas

# Creamos e inicializamos el SOM
som = MiniSom(som_size[0], som_size[1], 2, sigma=0.5, learning_rate=0.5)
som.random_weights_init(data)

# Entrenamos el SOM con los datos
som.train_random(data, 1000)  # Entrenamos durante 1000 iteraciones

# Visualizamos el SOM y los datos
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Distancias de las neuronas al BMU (Best Matching Unit)
plt.colorbar()

# Agregamos marcadores para los datos
for i, x in enumerate(data):
    bmu = som.winner(x)  # Encuentra la BMU para el dato actual
    plt.plot(bmu[0] + 0.5, bmu[1] + 0.5, 'ro', marker='o', markersize=5)  # Ubicamos el marcador en la BMU

plt.title('Mapa Autoorganizado de Kohonen')
plt.show()
