import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# Generar datos no linealmente separables
X, y = make_circles(n_samples=100, noise=0.1, random_state=42, factor=0.5)

# Crear el modelo SVM con un kernel no lineal (RBF)
svm = SVC(kernel='rbf', C=10, gamma=1)

# Entrenar el modelo
svm.fit(X, y)

# Crear una malla para visualizar la frontera de decisión
h = .02
x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predecir para cada punto en la malla
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])

# Graficar los resultados
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM con Kernel RBF')
plt.show()
