# Autor: Daniel Alejandro Flores Sepulveda
# Este programa realiza la extracción de información básica utilizando NLTK.

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

# Descargamos los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Función para extraer nombres de personas y ubicaciones
def extract_information(text):
    # Tokenizamos el texto en oraciones
    sentences = sent_tokenize(text)
    
    # Lista para almacenar nombres de personas y ubicaciones
    person_names = []
    locations = []
    
    # Recorremos las oraciones y extraemos nombres de personas y ubicaciones
    for sentence in sentences:
        # Tokenizamos la oración en palabras y asignamos etiquetas POS
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        
        # Buscamos nombres propios (etiqueta POS 'NNP') y ubicaciones (etiqueta POS 'NNP' seguida de 'IN' y 'NNP')
        for i in range(len(tagged_words)):
            if tagged_words[i][1] == 'NNP':
                person_names.append(tagged_words[i][0])
            elif tagged_words[i][1] == 'NNP' and i < len(tagged_words) - 2 and tagged_words[i+1][1] == 'IN' and tagged_words[i+2][1] == 'NNP':
                locations.append(tagged_words[i][0] + ' ' + tagged_words[i+2][0])
    
    return person_names, locations

# Texto de ejemplo para extraer información
sample_text = "Barack Obama was born in Honolulu, Hawaii. He served as the 44th President of the United States from 2009 to 2017."

# Realizamos la extracción de información
person_names, locations = extract_information(sample_text)

# Mostramos los resultados
print("Person names:", person_names)
print("Locations:", locations)
