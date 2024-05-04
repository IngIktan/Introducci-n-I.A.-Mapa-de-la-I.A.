# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo simple de representación de un espacio de estados en Python

class Estado:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

# Definir los estados del sistema
estado_inicial = Estado("Inicio", "Estado inicial del sistema")
estado_intermedio = Estado("Intermedio", "Estado intermedio del sistema")
estado_final = Estado("Fin", "Estado final del sistema")

# Representar el espacio de estados como un diccionario
espacio_estados = {
    estado_inicial.nombre: estado_inicial,
    estado_intermedio.nombre: estado_intermedio,
    estado_final.nombre: estado_final
}

# Acceder a un estado específico
print("Estado inicial:", espacio_estados["Inicio"].descripcion)
