# Autor: Daniel Alejandro Flores Sepulveda
# Este programa realiza el reconocimiento de objetos utilizando el modelo preentrenado MobileNetV2 en TensorFlow.


# Cargar la imagen original
img_rgb =cv2.imread('general.jpg')
img = cv2.imread('general.jpg')
imgb = cv2.imread('cara.png')
# Convertir la imagen a escala de grises
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Cargar la plantilla
template = cv2.imread('cara.png', 0)
# Obtener las dimensiones de la plantilla
w, h = template.shape[::-1]
# Realizar Template Matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# Establecer un umbral para obtener las ubicaciones de coincidencia
threshold = 0.8
loc = np.where(res >= threshold)
# Dibujar rectángulos alrededor de las coincidencias en la imagen original
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 255), 2)
# Mostrar las imágenes
cv2.imshow('Original', img)
cv2.imshow('Lo que buscamos', cv2.resize(imgb, (300, 250)))
cv2.imshow('Coincidencias', img_rgb)
# Guardar la imagen con las coincidencias resaltadas
cv2.imwrite('res.png', img_rgb)
# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()