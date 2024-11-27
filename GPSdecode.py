#Programme de réception du signal GPS émis via IP par le routeur UR35 (date, heure, latitude, longitude, vitesse, cap) 



import socket

#fonction de décodage

def parse_gprmc(nmea_sentence):
    fields = nmea_sentence.split(",")
    if fields[0] == "$GPRMC":

        #Heure UTC
        time = fields[1]
        heure_UTC = f"{time[:2]}:{time[2:4]}:{time[4:6]}"
        #Validité du fix
        validity = fields [2]
        valid = "Valide" if validity == "A" else "Invalide"
        if valid == "Invalide" :
            return None
        #Latitude
        latitude = convert_to_decimal (fields[3],fields[4])


        #longitude
        longitude = convert_to_decimal (fields [5], fields[6])
        
        #Vitesse au sol et conversion en Km/h
        vitesse_noeuds= float(fields[7])
        vitesse_kmh=vitesse_noeuds*1.852

        #Cap 
        cap = fields[8]
        
        #Date au format Français
        date = fields[9]
       
        date_formatee= f"{date[:2]}-{date [2:4]}-20{date[4:6]}"


        return {
            "Time (UTC)": heure_UTC,
            "Validation": valid,
            "Latitude" : latitude,
            "Longitude" : longitude,
            "Vitesse" : round(vitesse_kmh,2),
            "Cap" : cap,
            "date" : date_formatee,
        }
    return None

#Fonction de décodage des latitudes et longitude
def convert_to_decimal(coord, direction):
    # Vérifier si on traite la latitude (N/S) ou la longitude (E/W)
    if direction in ["N", "S"]:  # Latitude
        degrees = float(coord[:2])  # 2 premiers caractères pour les degrés
        minutes = float(coord[2:]) / 60  # Le reste pour les minutes
    elif direction in ["E", "W"]:  # Longitude
        degrees = float(coord[:3])  # 3 premiers caractères pour les degrés
        minutes = float(coord[3:]) / 60  # Le reste pour les minutes
    else:
        raise ValueError("Invalid direction")  # Gérer une éventuelle erreur

    decimal = degrees + minutes
    if direction in ["S", "W"]:  # Sud ou Ouest -> valeurs négatives
        decimal = -decimal
    return decimal


# Configurez l'adresse IP et le port de l'ordinateur de bord
IP = "192.168.1.100"  # Remplacez par l'IP de l'ordinateur de bord
PORT = 5051         # Assurez-vous que le port est le même que celui configuré sur le routeur 


#/Pour vérifier le port et l'adresse client il faut :
#  se connecter sur le réseau du routeur (WIFI ou ethernet)
# dans le navigateur se connecter à l'adresse 192.168.1.1
# Rentrer les identifiants et mot de passe 
# Dans le bandeau de gauche cliquer sur Industrial puis GPS
#Dans la fenêtre GPS dans le bandeau en haut de la page cliquer sur GPS IP forwarding
# Puis vérifier le tableau "Destination IP address"

# Créez un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print("En attente des données GPS...")
while True:
    data, addr = sock.recvfrom(1024)  # Taille de la trame
    print("Données reçues:", data.decode('utf-8'))
    GPRMC= data.decode('utf-8')
    print (GPRMC)
    GPS_GPRMC=parse_gprmc(GPRMC)
    if GPS_GPRMC == None :
        print ("Trame invalide")
    else :

        for key, value in GPS_GPRMC.items():
            print(f"{key}: {value}")



 
    