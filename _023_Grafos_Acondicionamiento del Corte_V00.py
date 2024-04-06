# Daniel Alejandro Flores Sepulveda
# Programa de Python para el Acondicionamiento del Corte

def acondicionamiento_corte(piezas):
    # Ordenar las piezas de mayor a menor longitud
    piezas_ordenadas = sorted(piezas, reverse=True)
    return piezas_ordenadas

# Ejemplo de uso
piezas = [10, 5, 8, 3, 6]
print("Piezas antes del acondicionamiento:", piezas)

piezas_ordenadas = acondicionamiento_corte(piezas)
print("Piezas después del acondicionamiento:", piezas_ordenadas)
#Este programa implementa una función llamada acondicionamiento_corte que realiza el acondicionamiento de corte de un conjunto de piezas. El acondicionamiento consiste en ordenar las piezas de mayor a menor longitud, lo que puede ayudar a reducir el desperdicio de material y optimizar el proceso de corte.

#En la primera columna, se proporciona el nombre del autor del programa y una descripción general del mismo.
#En la segunda columna, se encuentra el código Python.
#En la tercera columna, se agregan comentarios explicativos para cada línea de código.
#El programa primero imprime las piezas antes del acondicionamiento y luego imprime las piezas después del acondicionamiento para demostrar el efecto del proceso de ordenamiento.