# Autor: Daniel Alejandro Flores Sepulveda
# Este programa aplica un filtro a una imagen utilizando OpenCV.

import cv2

# Cargamos la imagen
image_path = 'imagen.jpg'
image = cv2.imread(image_path)

# Verificamos que la imagen se haya cargado correctamente
if image is None:
    print("Error al cargar la imagen.")
    exit()

# Definimos el kernel del filtro (en este caso, un filtro de suavizado)
kernel_size = (5, 5)  # Tamaño del kernel
kernel = cv2.getGaussianKernel(kernel_size[0], -1) * cv2.getGaussianKernel(kernel_size[1], -1).T

# Aplicamos el filtro a la imagen
filtered_image = cv2.filter2D(image, -1, kernel)

# Mostramos la imagen original y la imagen filtrada
cv2.imshow('Imagen Original', image)
cv2.imshow('Imagen Filtrada', filtered_image)

# Esperamos hasta que se presione una tecla y luego cerramos las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
