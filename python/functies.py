from classes import *

huidig_station = "Alkmaar"
totale_tijd = 0

def verbindingen_vinden(huidig_station, totale_tijd, traject, verbindingen):
    while totale_tijd < 120:
        # Zoek verbindingen die aansluiten bij het huidige station
        mogelijke_verbindingen = [
            v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
        ]

        # Stop als er geen mogelijke verbindingen meer zijn
        if not mogelijke_verbindingen:
            break

        # Vind de verbinding met de kortste reistijd
        kortste_verbinding = min(mogelijke_verbindingen, key=lambda v: v.tijd)

        # Controleer of de totale tijd binnen de limiet blijft
        if totale_tijd + kortste_verbinding.tijd > 120:
            break

        # Voeg de verbinding toe aan het traject
        traject.voeg_verbinding_toe(kortste_verbinding)
        totale_tijd += kortste_verbinding.tijd

        # Update het huidige station naar het andere station in de verbinding
        huidig_station = (
            kortste_verbinding.station2 if kortste_verbinding.station1 == huidig_station else kortste_verbinding.station1
        )

        # Verwijder de gebruikte verbinding uit de lijst van verbindingen
        verbindingen.remove(kortste_verbinding)

    return traject, totale_tijd

def bereken_totale_tijd(traject):
    # Bereken de totale reistijd van het traject.
    return sum(verbinding.tijd for verbinding in traject.traject)

def print_traject(traject):
    print(traject)
