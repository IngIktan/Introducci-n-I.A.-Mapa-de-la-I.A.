# Autor: Daniel Alejandro Flores Sepulveda
# Este programa simula un sistema de control de velocidad para un robot móvil utilizando el módulo Turtle en Python.

import turtle

# Inicializar la pantalla
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Control de Velocidad del Robot")

# Crear el objeto Turtle para el robot
robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.penup()

# Velocidad del robot y objetivo
velocidad_robot = 0  # Velocidad inicial
objetivo = 200  # Distancia objetivo

# Definir la función para controlar la velocidad del robot
def control_velocidad():
    global velocidad_robot
    # Calcular el error
    error = objetivo - robot.xcor()
    # Ajustar la velocidad proporcionalmente al error
    velocidad_robot = 0.1 * error

# Definir la función para mover el robot con la velocidad controlada
def mover():
    # Actualizar la posición del robot con la velocidad controlada
    robot.forward(velocidad_robot)
    # Llamar a la función de control de velocidad en cada paso
    control_velocidad()
    # Repetir el movimiento hasta alcanzar el objetivo
    if abs(robot.xcor() - objetivo) > 1:
        screen.ontimer(mover, 10)

# Iniciar el movimiento del robot
mover()

# Mantener la ventana abierta
turtle.done()
