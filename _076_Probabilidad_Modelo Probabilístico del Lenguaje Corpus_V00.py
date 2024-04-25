# Autor: Daniel Alejandro Flores Sepulveda
# Este programa carga un corpus de texto y calcula algunas estadísticas básicas.

import nltk
from nltk.corpus import brown

# Descargamos el corpus de Brown si no está disponible
nltk.download('brown')

# Cargamos el corpus de Brown
brown_corpus = brown.sents(categories='news')  # Seleccionamos solo una categoría del corpus, por ejemplo 'news'

# Convertimos el corpus en una lista plana de palabras
word_list = [word.lower() for sentence in brown_corpus for word in sentence]

# Calculamos la frecuencia de cada palabra en el corpus
word_freq = nltk.FreqDist(word_list)

# Calculamos la probabilidad de cada palabra en el corpus
total_words = len(word_list)
word_prob = {word: freq / total_words for word, freq in word_freq.items()}

# Mostramos algunas estadísticas básicas
print("Total de palabras en el corpus:", total_words)
print("Vocabulario único en el corpus:", len(word_freq))
print("Palabra más frecuente:", word_freq.most_common(1))
