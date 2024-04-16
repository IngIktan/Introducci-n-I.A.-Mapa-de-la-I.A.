# Daniel Alejandro Flores Sepulveda
# Programa para calcular la probabilidad a priori de un evento

# Definición de la función para calcular la probabilidad a priori
def probabilidad_a_priori(evento, espacio_muestral):
    apariciones_evento = espacio_muestral.count(evento)
    total_eventos = len(espacio_muestral)
    return apariciones_evento / total_eventos

# Definición del espacio muestral
espacio_muestral = ['cara', 'cruz', 'cara', 'cara', 'cruz', 'cara', 'cruz']

# Evento del cual se desea calcular la probabilidad a priori
evento = 'cara'

# Cálculo de la probabilidad a priori del evento
probabilidad = probabilidad_a_priori(evento, espacio_muestral)

# Impresión del resultado
print(f"La probabilidad a priori de obtener '{evento}' es: {probabilidad}")
