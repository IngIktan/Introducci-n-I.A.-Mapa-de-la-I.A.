import clips
from pyswip import Prolog

# Encadenamiento Hacia Adelante (Forward Chaining) con CLIPS
def encadenamiento_hacia_adelante():
    # Crear un entorno CLIPS
    env = clips.Environment()

    # Definir reglas y hechos
    env.build("""
        (defrule regla1
            (hecho1)
            =>
            (assert (conclusion1)))
        (defrule regla2
            (hecho2)
            =>
            (assert (conclusion2)))
    """)
    env.assert_string("(hecho1)")
    env.assert_string("(hecho2)")

    # Ejecutar el motor de inferencia hacia adelante
    env.run()

    # Consultar conclusiones
    for hecho in env.facts():
        print("Hecho:", hecho)

# Encadenamiento Hacia Atrás (Backward Chaining) con Prolog
def encadenamiento_hacia_atras():
    # Crear una instancia de Prolog
    prolog = Prolog()

    # Definir hechos y reglas
    prolog.assertz("padre(juan, maria)")
    prolog.assertz("padre(pedro, juan)")
    prolog.assertz("abuelo(X, Y) :- padre(X, Z), padre(Z, Y)")

    # Consulta utilizando encadenamiento hacia atrás
    meta = "abuelo(X, Y)"
    for solucion in prolog.query(meta):
        print("Solución para la meta '{}':".format(meta))
        print("X es abuelo de Y:", solucion["X"], solucion["Y"])

# Ejecutar encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
encadenamiento_hacia_adelante()

# Ejecutar encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
encadenamiento_hacia_atras()
