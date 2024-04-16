# Daniel Alejandro Flores Sepulveda
# Programa para calcular la regla de Bayes para un evento condicionado

# Definición de la función para calcular la regla de Bayes
def regla_de_bayes(probabilidad_A_dado_B, probabilidad_B, probabilidad_A):
    return (probabilidad_A_dado_B * probabilidad_B) / probabilidad_A

# Probabilidades proporcionadas
probabilidad_A_dado_B = 0.8  # P(A|B)
probabilidad_B = 0.3  # P(B)
probabilidad_A = 0.5  # P(A)

# Cálculo de la probabilidad P(B|A) utilizando la regla de Bayes
probabilidad_B_dado_A = regla_de_bayes(probabilidad_A_dado_B, probabilidad_B, probabilidad_A)

# Impresión del resultado
print("La probabilidad de B dado A es:", probabilidad_B_dado_A)
