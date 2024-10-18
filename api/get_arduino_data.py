'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07-10-2024
Developer:  Cristian Hernandez
'''

#Import libraries 
import serial
import time

#Arduino port
arduino_port = 'COM15'
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout=1
)

time.sleep(1) #delay

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip()
    
    if data:
        print(data)
        #temperature, humidity = data.split(",")
        
        #print(f"Temperature: {temperature}°C")
        #print(f"Humidity: {humidity}%")
        
    time.sleep(1)
