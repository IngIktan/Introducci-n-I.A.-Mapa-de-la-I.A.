# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Programa para implementar reglas de diagnóstico y causales

# Definir las reglas de diagnóstico y causales
reglas_diagnosticos = {
    "Síntoma1": ["EnfermedadA", "EnfermedadB"],
    "Síntoma2": ["EnfermedadA", "EnfermedadC"],
    # Añadir más reglas según sea necesario
}

reglas_causales = {
    "EnfermedadA": ["Causa1", "Causa2"],
    "EnfermedadB": ["Causa3", "Causa4"],
    # Añadir más reglas según sea necesario
}

# Función para realizar el diagnóstico
def diagnosticar(sintomas):
    enfermedades_posibles = set()
    for sintoma in sintomas:
        if sintoma in reglas_diagnosticos:
            enfermedades_posibles.update(reglas_diagnosticos[sintoma])
    
    return enfermedades_posibles

# Función para identificar las causas
def identificar_causas(enfermedades):
    causas_posibles = set()
    for enfermedad in enfermedades:
        if enfermedad in reglas_causales:
            causas_posibles.update(reglas_causales[enfermedad])
    
    return causas_posibles

# Ejemplo de uso
if __name__ == "__main__":
    sintomas_paciente = ["Síntoma1", "Síntoma2"]
    enfermedades = diagnosticar(sintomas_paciente)
    print("Enfermedades posibles:", enfermedades)

    causas = identificar_causas(enfermedades)
    print("Causas posibles:", causas)
