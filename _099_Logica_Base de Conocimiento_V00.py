# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa una base de conocimiento simple utilizando un diccionario en Python.

# Definir la base de conocimiento como un diccionario
base_conocimiento = {
    "perros": ["Labrador Retriever", "Bulldog", "Golden Retriever"],
    "gatos": ["Siamés", "Persa", "Maine Coon"],
    "aves": ["Canario", "Periquito", "Loro"],
    "peces": ["Betta", "Goldfish", "Guppy"]
}

# Función para buscar información en la base de conocimiento
def buscar_informacion(tema):
    if tema in base_conocimiento:
        print(f"Información sobre {tema}:")
        for item in base_conocimiento[tema]:
            print("-", item)
    else:
        print(f"No se encontró información sobre {tema}.")

# Ejemplos de consultas a la base de conocimiento
buscar_informacion("perros")
buscar_informacion("gatos")
buscar_informacion("aves")
buscar_informacion("peces")
buscar_informacion("reptiles")
