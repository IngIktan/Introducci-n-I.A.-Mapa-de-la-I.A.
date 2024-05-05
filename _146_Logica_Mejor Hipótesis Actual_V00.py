# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo básico de regresión lineal con Scikit-learn

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Características (una sola característica en este caso)
y = np.array([2, 4, 6, 8, 10])               # Etiquetas (valores a predecir)

# Inicializar el modelo de regresión lineal
regression_model = LinearRegression()

# Entrenar el modelo
regression_model.fit(X, y)

# Hacer predicciones
y_pred = regression_model.predict(X)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y, y_pred)

# Imprimir la pendiente (coeficiente) y el intercepto (ordenada al origen)
print("Pendiente:", regression_model.coef_)
print("Intercepto:", regression_model.intercept_)

# Imprimir el error cuadrático medio
print("Error cuadrático medio:", mse)
