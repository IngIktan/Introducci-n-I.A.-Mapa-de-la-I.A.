# Autor: Daniel Alejandro Flores Sepulveda
# Este programa detecta líneas en una imagen utilizando la transformada de Hough y etiqueta cada línea encontrada.
import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Aplicar la transformada de Hough para detectar líneas
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Convertir las coordenadas de las líneas a puntos
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        
        # Crear un array de puntos para la línea
        line_pts = np.array([[[x1, y1], [x2, y2]]], dtype=np.int32)
        
        # Dibujar la línea como contorno morado con un grosor mayor
        cv2.drawContours(image, [line_pts], -1, (255, 0, 255), thickness=5)

# Mostrar la imagen con las líneas detectadas
cv2.imshow('Lines Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
