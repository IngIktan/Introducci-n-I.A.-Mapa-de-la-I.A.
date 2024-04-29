# Autor: Daniel Alejandro Flores Sepulveda
# Ejemplo de representación y evaluación de proposiciones con cuantificadores en Python

# Definir un conjunto de elementos
elementos = [1, 2, 3, 4, 5]

# Ejemplo de proposición con cuantificador universal: "Todos los elementos son mayores que 0"
proposicion_universal = all(x > 0 for x in elementos)
print("Proposición con cuantificador universal:", proposicion_universal)

# Ejemplo de proposición con cuantificador existencial: "Al menos un elemento es par"
proposicion_existencial = any(x % 2 == 0 for x in elementos)
print("Proposición con cuantificador existencial:", proposicion_existencial)
