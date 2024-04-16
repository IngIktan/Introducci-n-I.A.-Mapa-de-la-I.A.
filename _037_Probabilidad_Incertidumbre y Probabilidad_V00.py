# Daniel Alejandro Flores Sepulveda
# Programa para ilustrar el concepto de incertidumbre en un contexto de decisiones

import random

# Definición de la función para simular una tirada de moneda (0: cara, 1: cruz)
def tirar_moneda():
    return random.choice([0, 1])

# Simulación de una tirada de moneda
resultado = tirar_moneda()

# Impresión del resultado
if resultado == 0:
    print("¡Cara!")
else:
    print("¡Cruz!")


# Ejecutar iteración de política y mostrar la política óptima resultante
optimal_policy = policy_iteration()
print("Política óptima:")
print(optimal_policy.reshape(n_rows, n_cols))
