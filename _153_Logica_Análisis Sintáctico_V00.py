# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo básico de un analizador sintáctico descendente recursivo en Python.

class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion_actual = 0

    def analizar(self):
        try:
            self.expr()
            print("Análisis sintáctico exitoso")
        except Exception as e:
            print("Error de análisis sintáctico:", e)

    def expr(self):
        self.match("PALABRA_RESERVADA", "if")
        self.match("IDENTIFICADOR")
        self.match("SIMBOLO", "==")
        self.match("NUMERO")
        self.match("SIMBOLO", ":")
        self.match("PALABRA_RESERVADA", "print")
        self.match("SIMBOLO", "(")
        self.match("CADENA")
        self.match("SIMBOLO", ")")

    def match(self, tipo_esperado, valor_esperado=None):
        token_actual = self.tokens[self.posicion_actual]
        if token_actual[0] == tipo_esperado:
            if valor_esperado is not None:
                if token_actual[1] == valor_esperado:
                    self.posicion_actual += 1
                else:
                    raise Exception(f"Se esperaba '{valor_esperado}' pero se encontró '{token_actual[1]}'")
            else:
                self.posicion_actual += 1
        else:
            raise Exception(f"Se esperaba un token de tipo '{tipo_esperado}' pero se encontró '{token_actual[0]}'")

# Tokens de ejemplo
tokens = [("PALABRA_RESERVADA", "if"), ("IDENTIFICADOR", "x"), ("SIMBOLO", "=="), ("NUMERO", "10"),
          ("SIMBOLO", ":"), ("PALABRA_RESERVADA", "print"), ("SIMBOLO", "("), ("CADENA", "'x es igual a 10'"),
          ("SIMBOLO", ")")]
# Crear instancia del analizador sintáctico
sintactico = AnalizadorSintactico(tokens)
# Analizar los tokens
sintactico.analizar()
