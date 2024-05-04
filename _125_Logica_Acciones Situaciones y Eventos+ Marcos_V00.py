# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de representación de acciones, situaciones y eventos utilizando marcos en Python

class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Accion: {self.nombre}'

class Situacion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Situacion: {self.nombre}'

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Evento: {self.nombre}'

class Marco:
    def __init__(self):
        self.relaciones = []

    def agregar_relacion(self, accion, situacion, evento):
        self.relaciones.append((accion, situacion, evento))

    def __str__(self):
        return f'Marco: {self.relaciones}'

# Crear instancias de acciones, situaciones y eventos
ir_a_comprar = Accion('Ir a comprar')
en_tienda = Situacion('En la tienda')
llegar_a_tienda = Evento('Llegar a la tienda')

# Crear un marco y agregar relaciones
marco = Marco()
marco.agregar_relacion(ir_a_comprar, en_tienda, llegar_a_tienda)

# Imprimir el marco
print(marco)
