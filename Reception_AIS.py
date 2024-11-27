# -*- coding: utf-8 -*-
# https://github.com/M0r13n/pyais Github de la librairie

import serial
from pyais import decode

# Connexion au port série
ser = serial.Serial('COM8', 9600, timeout=1) #Penser à modifier le port COM. 

def handle_navigation_data(message):
    """Extrait et utilise les informations pour éviter les collisions."""
    # Exemple de traitement de la position et de la vitesse
    if hasattr(message, 'lon') and hasattr(message, 'lat'):
        print(f"Position détectée - Lon: {message.lon}, Lat: {message.lat}")
    if hasattr(message, 'speed'):
        print(f"Vitesse détectée : {message.speed} nœuds")

# Lecture et décodage des données
while True:
    line = ser.readline().decode('ascii', errors='replace').strip()
    if line.startswith('!AIVDM'):
        try:
            # Décodage de la trame
            message = decode(line)
        
            # Identifier dynamiquement le type de message
            print(f"Type de message: {type(message).__name__}")
            print("Données du message décodé:")

            # Afficher dynamiquement tous les attributs du message
            for field, value in message.asdict().items():
                print(f"  {field}: {value}")

            # Traiter le message pour les actions de navigation
            handle_navigation_data(message)
        
        except Exception as e:
            print(f"Erreur de décodage pour la trame {line}: {e}")
