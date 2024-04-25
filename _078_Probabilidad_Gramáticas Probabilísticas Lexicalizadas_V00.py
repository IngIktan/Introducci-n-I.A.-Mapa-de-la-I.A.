# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa una gramática probabilística lexicalizada utilizando NLTK.

import nltk

# Definimos una gramática probabilística lexicalizada
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | 'John' [0.3] | 'Mary' [0.2]
    Det -> 'the' [0.7] | 'a' [0.3]
    N -> 'cat' [0.6] | 'dog' [0.4]
    VP -> V NP [0.5] | V [0.5]
    V -> 'chased' [0.9] | 'slept' [0.1]
""")

# Creamos un parser probabilístico con la gramática definida
parser = nltk.ViterbiParser(grammar)

# Parseamos una frase utilizando el parser probabilístico
sentence = "the cat chased the dog"
tokens = sentence.split()
parsed_trees = parser.parse(tokens)

# Mostramos los árboles de parseo generados por el parser
for tree in parsed_trees:
    print("Árbol de Parseo:", tree)
