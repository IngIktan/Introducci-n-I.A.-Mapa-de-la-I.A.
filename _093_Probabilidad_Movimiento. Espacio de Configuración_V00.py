# Autor: Daniel Alejandro Flores Sepulveda
# Este programa visualiza el espacio de configuración para un robot móvil simple en un plano XY.

import numpy as np
import matplotlib.pyplot as plt

# Definir los límites del espacio de configuración
x_min, x_max = -5, 5
y_min, y_max = -5, 5

# Crear una malla de puntos en el espacio de configuración
x_values = np.linspace(x_min, x_max, 100)
y_values = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x_values, y_values)

# Visualizar el espacio de configuración
plt.figure(figsize=(8, 6))
plt.title('Espacio de Configuración para un Robot Móvil en un Plano XY')
plt.xlabel('Posición en X')
plt.ylabel('Posición en Y')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.gca().set_aspect('equal', adjustable='box')

# Dibujar el espacio de configuración
plt.scatter(X, Y, s=5, color='blue')
plt.grid(True)
plt.show()
