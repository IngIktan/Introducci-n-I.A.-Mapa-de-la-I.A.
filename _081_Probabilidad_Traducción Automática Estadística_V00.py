# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa un traductor automático estadístico muy básico utilizando NLTK.

import nltk
from nltk.corpus import europarl_raw

# Descargamos los datos del corpus paralelo Europarl para inglés y español
nltk.download('europarl_raw')

# Cargamos los datos del corpus paralelo
en_es_sentences = europarl_raw.sents('es', 'en')

# Creamos diccionarios para almacenar las frecuencias de las palabras
en_freq = {}
es_freq = {}

# Contamos las frecuencias de las palabras en inglés y español
for sentence in en_es_sentences:
    en_words = [word.lower() for word in sentence[0].split()]
    es_words = [word.lower() for word in sentence[1].split()]
    for word in en_words:
        en_freq[word] = en_freq.get(word, 0) + 1
    for word in es_words:
        es_freq[word] = es_freq.get(word, 0) + 1

# Función de traducción
def translate_sentence(sentence, source_lang, target_lang):
    translated_sentence = []
    if source_lang == 'en' and target_lang == 'es':
        for word in sentence.split():
            translated_sentence.append(word if word not in en_freq else max(en_es_sentences, key=lambda x: en_freq.get(x, 0)))
    elif source_lang == 'es' and target_lang == 'en':
        for word in sentence.split():
            translated_sentence.append(word if word not in es_freq else max(en_es_sentences, key=lambda x: es_freq.get(x, 0)))
    else:
        print("Unsupported language pair.")
    return ' '.join(translated_sentence)

# Ejemplo de traducción
sentence_to_translate = "Hello, how are you?"
translated_sentence = translate_sentence(sentence_to_translate, 'en', 'es')
print("Translated sentence:", translated_sentence)
