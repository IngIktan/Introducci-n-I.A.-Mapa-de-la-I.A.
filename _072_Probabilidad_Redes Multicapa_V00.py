# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa una red neuronal multicapa para clasificación binaria utilizando TensorFlow.

import numpy as np
import tensorflow as tf

# Generamos datos aleatorios para probar la red neuronal
num_samples = 1000
num_features = 2
X = np.random.rand(num_samples, num_features)  # Generamos 1000 muestras con 2 características
y = np.random.randint(2, size=num_samples)  # Generamos etiquetas binarias aleatorias

# Definimos el modelo de red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(num_features,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilamos el modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entrenamos el modelo
model.fit(X, y, epochs=10, batch_size=32)

# Evaluamos el modelo
loss, accuracy = model.evaluate(X, y)
print("Accuracy:", accuracy)
