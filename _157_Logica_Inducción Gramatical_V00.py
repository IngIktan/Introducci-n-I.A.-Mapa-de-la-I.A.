# Autor: Daniel Alejandro Flores Sepulveda
# introduccion de la gramática
import nltk
from nltk import Nonterminal, induce_pcfg
from nltk.corpus import treebank

import nltk
nltk.download('treebank')

# Obtener las producciones de la gramática a partir de un corpus etiquetado
productions = []
for tree in treebank.parsed_sents():
    tree.collapse_unary(collapsePOS=False)
    tree.chomsky_normal_form()
    productions += tree.productions()

# Inducir una gramática PCFG a partir de las producciones
S = Nonterminal('S')
grammar = induce_pcfg(S, productions)

# Imprimir la gramática inducida
print(grammar)
