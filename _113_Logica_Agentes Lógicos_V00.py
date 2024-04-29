# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de un agente lógico que responde a consultas sobre hechos lógicos

# Definir una base de conocimiento de hechos
base_conocimiento = {
    "llueve": True,
    "hace_sol": False,
    "temperatura": 25,
    # Agregar más hechos según sea necesario
}

# Función para consultar un hecho en la base de conocimiento
def consultar_hecho(hecho):
    if hecho in base_conocimiento:
        return base_conocimiento[hecho]
    else:
        return "No sé"

# Ejemplo de uso
if __name__ == "__main__":
    # Consultar si llueve
    print("¿Llueve?", consultar_hecho("llueve"))

    # Consultar si hace sol
    print("¿Hace sol?", consultar_hecho("hace_sol"))

    # Consultar la temperatura
    print("Temperatura:", consultar_hecho("temperatura"))

    # Consultar un hecho desconocido
    print("¿El viento está soplando?", consultar_hecho("viento"))
