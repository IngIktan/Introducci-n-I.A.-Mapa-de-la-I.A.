# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo básico de un analizador léxico en Python.

class AnalizadorLexico:
    def __init__(self, texto):
        self.texto = texto
        self.tokens = []
        self.palabras_reservadas = ["if", "else", "while", "for", "int", "float", "return"]  # Ejemplo de palabras reservadas

    def analizar(self):
        i = 0
        while i < len(self.texto):
            if self.texto[i].isspace():
                i += 1
            elif self.texto[i].isalpha():
                token = ""
                while i < len(self.texto) and (self.texto[i].isalpha() or self.texto[i].isdigit()):
                    token += self.texto[i]
                    i += 1
                if token in self.palabras_reservadas:
                    self.tokens.append(("PALABRA_RESERVADA", token))
                else:
                    self.tokens.append(("IDENTIFICADOR", token))
            elif self.texto[i].isdigit():
                num = ""
                while i < len(self.texto) and self.texto[i].isdigit():
                    num += self.texto[i]
                    i += 1
                self.tokens.append(("NUMERO", num))
            else:
                self.tokens.append(("SIMBOLO", self.texto[i]))
                i += 1
        return self.tokens

# Texto de ejemplo
texto = "if x == 10:\n    print('x es igual a 10')"
# Crear instancia del analizador léxico
lexico = AnalizadorLexico(texto)
# Analizar el texto
tokens = lexico.analizar()
# Imprimir los tokens obtenidos
print("Tokens:", tokens)
