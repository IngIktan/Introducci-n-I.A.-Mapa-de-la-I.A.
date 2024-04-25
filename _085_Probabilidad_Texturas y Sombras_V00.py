# Autor: Daniel Alejandro Flores Sepulveda
# Este programa crea una escena con textura y sombra utilizando Pygame.

import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos el tamaño de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Texturas y Sombras')

# Cargamos la imagen de la textura y la sombra
texture_img = pygame.image.load('texture.jpg').convert()
shadow_img = pygame.image.load('shadow.png').convert_alpha()

# Escalamos la sombra para que coincida con el tamaño de la ventana
shadow_img = pygame.transform.scale(shadow_img, (window_width, window_height))

# Configuramos la posición de la textura y la sombra
texture_pos = (100, 100)
shadow_pos = (200, 200)

# Ciclo principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujamos la textura y la sombra en la ventana
    window.blit(texture_img, texture_pos)
    window.blit(shadow_img, shadow_pos)

    # Actualizamos la ventana
    pygame.display.update()
