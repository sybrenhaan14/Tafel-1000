from classes import *

huidig_station = "Alkmaar"
totale_tijd = 0

# Maak een nieuw traject object aan
traject = Traject(traject_id=1, totale_tijd=0)  

while totale_tijd < 120:
    # Vind verbindingen met huidig station
    mogelijke_verbindingen = [
        v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
    ]

    # Als er geen mogelijke verbindingen zijn dan stoppen
    if not mogelijke_verbindingen:
        break

    # Vind verbinding met de kortste tijd
    kortste_verbinding = min(mogelijke_verbindingen, key=lambda v: v.tijd)

    # Controleer of toevoegen van verbinding binnen limiet blijft
    if totale_tijd + kortste_verbinding.tijd > 120:
        break

    # Voeg de verbinding toe aan het traject
    traject.voeg_verbinding_toe(kortste_verbinding)

    # Update de totale tijd met de tijd van de verbinding
    totale_tijd += kortste_verbinding.tijd

    # Update huidig station naar het andere station in de gekozen verbinding
    if kortste_verbinding.station1 == huidig_station:
        huidig_station = kortste_verbinding.station2
    else:
        huidig_station = kortste_verbinding.station1

    # Verwijder de gebruikte verbinding
    verbindingen.remove(kortste_verbinding)

# Bereken de totale tijd van het traject
traject.totale_tijd = traject.bereken_totale_tijd()