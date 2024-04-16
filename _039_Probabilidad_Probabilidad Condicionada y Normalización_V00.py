# Daniel Alejandro Flores Sepulveda
# Programa para calcular la probabilidad condicionada y realizar la normalización

# Definición de la función para calcular la probabilidad condicionada
def probabilidad_condicionada(evento_A, evento_B, espacio_muestral):
    ocurrencias_A_y_B = espacio_muestral.count((evento_A, evento_B))
    ocurrencias_B = espacio_muestral.count((evento_B,))
    if ocurrencias_B == 0:
        return 0  # Evitar división por cero
    return ocurrencias_A_y_B / ocurrencias_B

# Definición de la función para normalizar una lista de probabilidades
def normalizar(probabilidades):
    total = sum(probabilidades)
    return [p / total for p in probabilidades]

# Definición del espacio muestral
espacio_muestral = [('cara', 'uno'), ('cruz', 'dos'), ('cara', 'tres'), ('cruz', 'uno'), ('cara', 'dos')]

# Eventos para calcular la probabilidad condicionada
evento_A = 'cara'
evento_B = 'uno'

# Cálculo de la probabilidad condicionada
probabilidad = probabilidad_condicionada(evento_A, evento_B, espacio_muestral)

# Impresión del resultado
print(f"La probabilidad condicionada de '{evento_A}' dado '{evento_B}' es: {probabilidad}")

# Ejemplo de normalización de probabilidades
probabilidades = [0.2, 0.3, 0.5]
probabilidades_normalizadas = normalizar(probabilidades)
print("Probabilidades normalizadas:", probabilidades_normalizadas)
