# Autor: Daniel Alejandro Flores Sepulveda
# Este programa crea una escena con textura y sombra utilizando Pygame, con movimiento controlado por teclado.

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

# Configuramos la posición inicial de la textura y la sombra
texture_pos = [100, 100]
shadow_pos = [200, 200]

# Velocidad de movimiento
movement_speed = 5

# Ciclo principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas presionadas
    keys = pygame.key.get_pressed()
    
    # Mover la textura y la sombra según las teclas presionadas
    if keys[pygame.K_LEFT]:
        texture_pos[0] -= movement_speed
        shadow_pos[0] -= movement_speed
    if keys[pygame.K_RIGHT]:
        texture_pos[0] += movement_speed
        shadow_pos[0] += movement_speed
    if keys[pygame.K_UP]:
        texture_pos[1] -= movement_speed
        shadow_pos[1] -= movement_speed
    if keys[pygame.K_DOWN]:
        texture_pos[1] += movement_speed
        shadow_pos[1] += movement_speed

    # Limpiar la ventana
    window.fill((0, 0, 0))
    
    # Dibujar la sombra y la textura en la ventana
    window.blit(shadow_img, shadow_pos)
    window.blit(texture_img, texture_pos)

    # Actualizar la ventana
    pygame.display.update()
