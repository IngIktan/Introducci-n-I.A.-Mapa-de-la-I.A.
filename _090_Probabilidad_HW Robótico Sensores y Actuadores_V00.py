# Autor: Daniel Alejandro Flores Sepulveda
# Este programa simula el control de un LED utilizando un botón como sensor.

import time

# Mock de la biblioteca RPi.GPIO
class MockGPIO:
    OUT = "OUT"
    IN = "IN"
    FALLING = "FALLING"
    PUD_UP = "PUD_UP"
    BCM = "BCM"

    @staticmethod
    def setmode(mode):
        pass

    @staticmethod
    def setup(pin, direction, **kwargs):
        pass

    @staticmethod
    def output(pin, value):
        pass

    @staticmethod
    def input(pin):
        return True

    @staticmethod
    def add_event_detect(pin, edge, callback=None, bouncetime=None):
        pass

    @staticmethod
    def cleanup():
        pass

# Utilizar el MockGPIO en lugar de RPi.GPIO
GPIO = MockGPIO

# Definir los pines GPIO
LED_PIN = 17  # Conectar el LED al pin GPIO 17
BUTTON_PIN = 27  # Conectar el botón al pin GPIO 27

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Función para cambiar el estado del LED
def toggle_led(channel):
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))

# Asociar la función toggle_led al evento de presionar el botón
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=toggle_led, bouncetime=200)

try:
    # Bucle principal
    while True:
        # El programa espera en este bucle
        time.sleep(0.1)

except KeyboardInterrupt:
    # Manejar la interrupción de teclado (Ctrl+C)
    print("Programa detenido por el usuario.")
    # Apagar el LED antes de salir
    GPIO.output(LED_PIN, False)
    # Limpiar los pines GPIO
    GPIO.cleanup()
