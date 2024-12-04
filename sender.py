import serial
import time

# Configuration du port série
# port = 'COM5'  # Changez selon votre système (ex : COM3 sur Windows)
port = '/dev/ttyUSB0'  # Changez selon votre système (ex : COM4 sur Windows)

baudrate = 9600

ser = serial.Serial(port, baudrate, timeout=1)
print(f"Module connecté sur {port} à {baudrate} baud.")

try:
    while True:
        message = "Hello LoRa, message envoyé à " + str(time.time())
        ser.write(message.encode())  # Envoie le message
        print(f"Envoyé : {message}")
        time.sleep(2)  # Attendre 2 secondes avant d'envoyer un autre message
except KeyboardInterrupt:
    print("Arrêt de l'émetteur.")
finally:
    ser.close()
