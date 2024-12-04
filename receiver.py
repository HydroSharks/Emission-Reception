import serial

# Configuration du port série
port = 'COM12'  # Changez selon votre système (ex : COM4 sur Windows)
baudrate = 9600

ser = serial.Serial(port, baudrate, timeout=1)
print(f"Module connecté sur {port} à {baudrate} baud.")

try:
    while True:
        if ser.in_waiting > 0:  # Vérifie si des données sont disponibles
            message = ser.readline().decode().strip()  # Lit et décode les données
            print(f"Reçu : {message}")
except KeyboardInterrupt:
    print("Arrêt du récepteur.")
finally:
    ser.close()
