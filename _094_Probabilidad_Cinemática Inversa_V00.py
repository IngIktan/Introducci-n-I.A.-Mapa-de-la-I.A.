# Autor: Daniel Alejandro Flores Sepulveda
# Este programa calcula la cinemática inversa de un robot de 2 grados de libertad en el plano XY.

import numpy as np

# Función para calcular la cinemática inversa
def inverse_kinematics(x, y, l1, l2):
    # Calcular la distancia al extremo del brazo
    d = np.sqrt(x**2 + y**2)
    
    # Calcular el ángulo de la primera articulación
    theta1 = np.arctan2(y, x)
    
    # Calcular el ángulo de la segunda articulación utilizando el teorema del coseno
    cos_theta2 = (l1**2 + l2**2 - d**2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    # Devolver los ángulos en radianes
    return theta1, theta2

# Coordenadas deseadas del extremo del robot
x_deseado = 2
y_deseado = 2

# Longitudes de los eslabones del brazo
l1 = 2
l2 = 2

# Calcular la cinemática inversa
theta1, theta2 = inverse_kinematics(x_deseado, y_deseado, l1, l2)

# Imprimir los resultados
print("Ángulo de la articulación 1:", np.degrees(theta1))
print("Ángulo de la articulación 2:", np.degrees(theta2))
