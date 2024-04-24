# Autor: Daniel Alejandro Flores Sepulveda
# Programa para reconocimiento de voz utilizando la biblioteca SpeechRecognition

import speech_recognition as sr

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Capturar audio del micrófono
with sr.Microphone() as source:
    print("Diga algo:")
    audio = recognizer.listen(source)

# Reconocer texto a partir del audio
try:
    text = recognizer.recognize_google(audio, language="es-ES")
    print("Texto reconocido:", text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error al conectarse al servicio de reconocimiento de voz:", e)
