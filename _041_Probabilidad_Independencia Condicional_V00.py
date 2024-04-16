# Daniel Alejandro Flores Sepulveda
# Programa para verificar la independencia condicional entre dos eventos dados un espacio muestral

# Definición de la función para verificar la independencia condicional
def independencia_condicional(evento_A, evento_B, evento_C, espacio_muestral):
    ocurrencias_A_y_B_y_C = espacio_muestral.count((evento_A, evento_B, evento_C))
    ocurrencias_A_y_C = espacio_muestral.count((evento_A, evento_C))
    if ocurrencias_A_y_C == 0:
        return False  # Evitar división por cero
    return ocurrencias_A_y_B_y_C / ocurrencias_A_y_C == espacio_muestral.count((evento_B, evento_C)) / ocurrencias_A_y_C

# Definición del espacio muestral
espacio_muestral = [('cara', 'uno', 'sol'), ('cara', 'dos', 'sol'), ('cruz', 'uno', 'nublado'), ('cara', 'dos', 'nublado'), ('cara', 'uno', 'sol')]

# Eventos para verificar la independencia condicional
evento_A = 'cara'
evento_B = 'dos'
evento_C = 'sol'

# Verificación de la independencia condicional
independencia = independencia_condicional(evento_A, evento_B, evento_C, espacio_muestral)

# Impresión del resultado
if independencia:
    print(f"Los eventos '{evento_A}' y '{evento_B}' son independientes condicionalmente a '{evento_C}'.")
else:
    print(f"Los eventos '{evento_A}' y '{evento_B}' no son independientes condicionalmente a '{evento_C}'.")
