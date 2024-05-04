# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de un sistema experto básico sin bibliotecas externas en Python

class SistemaExperto:
    """Clase que define el motor de inferencia del sistema experto"""

    @staticmethod
    def diagnostico(sintomas):
        """Función para diagnosticar la enfermedad basada en los síntomas"""

        # Comprobación de los síntomas y asignación del diagnóstico
        if sintomas["fiebre"] and sintomas["tos"]:
            return "gripe"
        elif sintomas["fiebre"] and sintomas["dolor_garganta"]:
            return "faringitis"
        elif sintomas["dolor_cabeza"] and sintomas["cansancio"]:
            return "migraña"
        else:
            return "No se pudo determinar la enfermedad"

if __name__ == "__main__":
    # Síntomas del paciente
    sintomas_paciente = {
        "fiebre": True,
        "tos": True,
        "dolor_garganta": False,
        "dolor_cabeza": False,
        "cansancio": False
    }

    # Crear instancia del sistema experto
    sistema_experto = SistemaExperto()

    # Obtener el diagnóstico
    diagnostico = sistema_experto.diagnostico(sintomas_paciente)

    # Imprimir el diagnóstico
    print("Diagnóstico:", diagnostico)
