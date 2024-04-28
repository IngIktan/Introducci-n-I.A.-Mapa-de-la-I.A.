# Autor: Daniel Alejandro Flores Sepulveda
# Este programa simula el movimiento de un robot utilizando el módulo Turtle en Python.

import turtle

# Inicializar la pantalla
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Robot Simulator")

# Crear el objeto Turtle para el robot
robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.penup()

# Definir las funciones para el movimiento del robot
def move_forward():
    robot.forward(50)

def move_backward():
    robot.backward(50)

def turn_left():
    robot.left(90)

def turn_right():
    robot.right(90)

# Asociar las teclas del teclado con las funciones de movimiento
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")

# Habilitar la escucha de eventos del teclado
screen.listen()

# Mantener la ventana abierta
turtle.done()
