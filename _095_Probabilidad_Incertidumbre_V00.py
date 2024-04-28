# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa un Filtro de Kalman para estimar la posición de un robot móvil en un entorno 1D.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
dt = 0.1  # Intervalo de tiempo entre mediciones
t = np.arange(0, 10, dt)  # Tiempo de simulación
n = len(t)  # Número de pasos de tiempo
velocidad_real = 1  # Velocidad real del robot
std_a = 0.1  # Desviación estándar del ruido de aceleración
std_z = 0.5  # Desviación estándar del ruido de medición

# Función de transición de estado
def estado_transicion(x, v, dt):
    return x + v * dt

# Función de observación
def observacion(x, std):
    return x + np.random.randn() * std

# Inicialización del filtro de Kalman
x_est = np.zeros(n)  # Estado estimado
v_est = np.zeros(n)  # Velocidad estimada
x_pred = np.zeros(n)  # Predicción del estado
v_pred = np.zeros(n)  # Predicción de la velocidad
P = np.zeros(n)  # Covarianza de la estimación

# Condiciones iniciales
x_est[0] = 0
v_est[0] = 0
P[0] = 1

# Iteración del filtro de Kalman
for i in range(1, n):
    # Predicción del estado y covarianza
    x_pred[i] = estado_transicion(x_est[i-1], v_est[i-1], dt)
    v_pred[i] = v_est[i-1]
    P[i] = P[i-1] + std_a**2

    # Actualización del estado y covarianza
    K = P[i] / (P[i] + std_z**2)
    z = observacion(x_pred[i], std_z)
    x_est[i] = x_pred[i] + K * (z - x_pred[i])
    v_est[i] = v_pred[i] + K * (z - x_pred[i])

# Visualización de los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, x_est, label='Posición Estimada')
plt.plot(t, v_est, label='Velocidad Estimada')
plt.plot(t, [velocidad_real]*n, '--', label='Velocidad Real')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Filtro de Kalman para Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()
