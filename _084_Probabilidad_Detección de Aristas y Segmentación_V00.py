# Autor: Daniel Alejandro Flores Sepulveda
# Este programa realiza detección de bordes y segmentación en tiempo real utilizando OpenCV con la cámara.

import cv2

# Creamos un objeto capturador de video
cap = cv2.VideoCapture(0)

# Verificamos que la cámara se haya inicializado correctamente
if not cap.isOpened():
    print("Error al inicializar la cámara.")
    exit()

# Ciclo principal para capturar video en tiempo real
while True:
    # Capturamos un fotograma de la cámara
    ret, frame = cap.read()

    # Convertimos el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicamos el algoritmo de detección de bordes (Canny)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    # Encontramos los contornos en la imagen binaria de bordes
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujamos los contornos encontrados en el fotograma original
    frame_with_contours = cv2.drawContours(frame.copy(), contours, -1, (0, 255, 0), 2)

    # Mostramos el fotograma original y el fotograma con los contornos
    cv2.imshow('Camara', frame)
    cv2.imshow('Contornos', frame_with_contours)

    # Esperamos hasta que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos los recursos y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
