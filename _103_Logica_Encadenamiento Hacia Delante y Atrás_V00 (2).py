# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa encadenamiento hacia adelante y hacia atrás en lógica proposicional.

# Reglas: A -> B, B -> C
reglas = {'A': 'B', 'B': 'C'}

# Hechos iniciales
hechos = {'A'}

# Función para encadenamiento hacia adelante
def encadenamiento_hacia_adelante(reglas, hechos):
    while True:
        nuevo_hecho_agregado = False
        for antecedente, consecuente in reglas.items():
            if antecedente in hechos and consecuente not in hechos:
                hechos.add(consecuente)
                nuevo_hecho_agregado = True
        if not nuevo_hecho_agregado:
            break
    return hechos

# Función para encadenamiento hacia atrás
def encadenamiento_hacia_atras(reglas, objetivo, hechos):
    if objetivo in hechos:
        return True
    for antecedente, consecuente in reglas.items():
        if consecuente == objetivo:
            if encadenamiento_hacia_atras(reglas, antecedente, hechos):
                return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    # Realizar encadenamiento hacia adelante
    hechos_adelante = encadenamiento_hacia_adelante(reglas, hechos.copy())
    print("Hechos obtenidos mediante encadenamiento hacia adelante:", hechos_adelante)

    # Realizar encadenamiento hacia atrás para verificar si C es alcanzable
    objetivo = 'C'
    if encadenamiento_hacia_atras(reglas, objetivo, hechos.copy()):
        print(f"{objetivo} es alcanzable mediante encadenamiento hacia atrás.")
    else:
        print(f"{objetivo} no es alcanzable mediante encadenamiento hacia atrás.")
