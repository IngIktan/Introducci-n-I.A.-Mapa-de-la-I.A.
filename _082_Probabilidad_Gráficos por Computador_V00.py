# Autor: Daniel Alejandro Flores Sepulveda
# Este programa utiliza Pygame para dibujar un círculo en una ventana.

import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos el tamaño de la ventana
window_width = 800
window_height = 600
window_size = (window_width, window_height)

# Creamos la ventana
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Dibujando un círculo')

# Definimos el color del círculo (en formato RGB)
circle_color = (255, 0, 0)  # Rojo

# Definimos las coordenadas del centro del círculo
circle_center = (window_width // 2, window_height // 2)

# Definimos el radio del círculo
circle_radius = 50

# Ciclo principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Limpiamos la ventana
    window.fill((255, 255, 255))  # Color blanco
    
    # Dibujamos el círculo
    pygame.draw.circle(window, circle_color, circle_center, circle_radius)
    
    # Actualizamos la pantalla
    pygame.display.flip()
