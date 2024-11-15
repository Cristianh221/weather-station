import random
import time
import requests

# Datos de acceso a ThingSpeak
CHANNEL_ID = '2734194' 
WRITE_API_KEY = 'XCICDYJMGU0XC4WX'  

# URL de la API para enviar datos
THINGSPEAK_URL = f'https://api.thingspeak.com/update'

# Inicializar las variables para almacenar el último valor de temperatura y humedad
last_temperature = -11  # Un valor menor que el mínimo posible (-10)
last_humidity = -1  # Un valor menor que el mínimo posible (0)

# Función para enviar los datos a ThingSpeak
def send_data_to_thingspeak(temperature, humidity):
    payload = {
        'api_key': WRITE_API_KEY,
        'field1': temperature,  # Campo 1 es para la temperatura
        'field2': humidity      # Campo 2 es para la humedad
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=payload)
        if response.status_code == 200:
            print(f"Datos enviados correctamente: Temp = {temperature}°C, Humedad = {humidity}%")
        else:
            print(f"Error al enviar los datos: {response.status_code}")
    except Exception as e:
        print(f"Error en la conexión con ThingSpeak: {e}")

# Bucle principal para generar y enviar datos cada 3 segundos
while True:
    # Generar valores aleatorios
    temperature = random.uniform(-10, 100)  # Temperatura entre -10 y 100 grados
    humidity = random.uniform(0, 100)  # Humedad entre 0% y 100%

    # Comparar si los nuevos valores son mayores que los últimos enviados
    if temperature > last_temperature or humidity > last_humidity:
        send_data_to_thingspeak(temperature, humidity)
        last_temperature = temperature
        last_humidity = humidity

    # Esperar 3 segundos antes de generar nuevos valores
    time.sleep(3)