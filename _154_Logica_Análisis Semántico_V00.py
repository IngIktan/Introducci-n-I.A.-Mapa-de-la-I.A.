# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo básico de un analizador semántico en Python.

class AnalizadorSemantico:
    def __init__(self, arbol_sintactico):
        self.arbol_sintactico = arbol_sintactico

    def analizar(self):
        try:
            self.validar(self.arbol_sintactico)
            print("Análisis semántico exitoso")
        except Exception as e:
            print("Error de análisis semántico:", e)

    def validar(self, nodo):
        if nodo.tipo == "if_statement":
            condicion = nodo.hijos[0]
            if condicion.tipo == "condicion":
                self.validar_expresion(condicion)
            elif condicion.tipo == "variable":
                self.validar_variable(condicion)
            else:
                raise Exception("Condición no válida")
        elif nodo.tipo == "print_statement":
            mensaje = nodo.hijos[0]
            if mensaje.tipo != "cadena":
                raise Exception("El mensaje de impresión debe ser una cadena")

    def validar_expresion(self, expresion):
        operador = expresion.valor
        if operador not in ["==", "!=", "<", ">"]:
            raise Exception(f"Operador '{operador}' no válido")

        izquierda = expresion.hijos[0]
        derecha = expresion.hijos[1]

        if izquierda.tipo != "variable":
            raise Exception("Lado izquierdo de la expresión debe ser una variable")

        if derecha.tipo == "variable":
            self.validar_variable(derecha)
        elif derecha.tipo == "numero":
            pass
        else:
            raise Exception("Lado derecho de la expresión debe ser una variable o un número")

    def validar_variable(self, variable):
        # Aquí podrías agregar lógica para verificar si la variable existe en el contexto o tiene el tipo adecuado, etc.
        pass

# Clase para representar nodos del árbol sintáctico
class Nodo:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos else []

# Crear un árbol sintáctico de ejemplo
arbol_sintactico = Nodo("if_statement", hijos=[
    Nodo("condicion", valor="==", hijos=[
        Nodo("variable", valor="x"),
        Nodo("numero", valor="10")
    ]),
    Nodo("print_statement", hijos=[
        Nodo("cadena", valor="'x es igual a 10'")
    ])
])

# Crear instancia del analizador semántico y analizar el árbol sintáctico
semantico = AnalizadorSemantico(arbol_sintactico)
semantico.analizar()
