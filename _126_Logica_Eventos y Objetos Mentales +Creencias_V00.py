# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de representación de creencias como objetos mentales en Python

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Evento: {self.nombre}'

class ObjetoMental:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Objeto Mental: {self.nombre}'

class Creencia:
    def __init__(self, sujeto, evento, objeto_mental):
        self.sujeto = sujeto
        self.evento = evento
        self.objeto_mental = objeto_mental

    def __str__(self):
        return f'Creencia: {self.sujeto} cree que {self.evento} implica {self.objeto_mental}'

# Crear instancias de eventos y objetos mentales
llegada_amigo = Evento('Llegada de un amigo')
esperanza = ObjetoMental('Esperanza')

# Crear una creencia
creencia = Creencia('Juan', llegada_amigo, esperanza)

# Imprimir la creencia
print(creencia)
