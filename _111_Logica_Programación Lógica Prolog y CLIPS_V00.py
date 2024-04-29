# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: clips 

import clips

# Crear un entorno CLIPS
env = clips.Environment()

# Cargar reglas y hechos
env.build("""
    (defrule regla-ejemplo
        (hijo-de ?hijo ?padre)
        =>
        (assert (es-hijo-de ?hijo ?padre)))
""")
env.assert_string("(hijo-de juan pedro)")

# Ejecutar el motor de inferencia
env.run()

# Consulta
for hecho in env.facts():
    if hecho.template.name == "es-hijo-de":
        print(hecho[1], "es hijo de", hecho[2])
