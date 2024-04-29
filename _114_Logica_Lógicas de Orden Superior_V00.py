# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de funciones de orden superior en Python

# Función de orden superior que toma una función como argumento
def aplicar_funcion(funcion, argumento):
    return funcion(argumento)

# Función de ejemplo para ser utilizada como argumento
def cuadrado(numero):
    return numero ** 2

# Llamada a la función de orden superior con la función cuadrado como argumento
resultado = aplicar_funcion(cuadrado, 5)
print("Resultado:", resultado)
