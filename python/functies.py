from classes import *


def vind_mogelijke_verbindingen(huidig_station, verbindingen):
    #Zoek verbindingen die aansluiten bij het huidige station
    return [
        v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
    ]

def vind_kortste_verbinding(mogelijke_verbindingen):
    #Vind de verbinding met de kortste reistijd
    return min(mogelijke_verbindingen, key=lambda v: v.tijd)

def update_huidig_station(huidig_station, kortste_verbinding):
    #Werk het huidige station bij op basis van de verbinding
    return kortste_verbinding.station2 if kortste_verbinding.station1 == huidig_station else kortste_verbinding.station1

def voeg_verbinding_toe_en_update_tijd(traject, kortste_verbinding, totale_tijd):
    #Voeg de verbinding toe aan het traject en werk de totale tijd bij
    traject.voeg_verbinding_toe(kortste_verbinding)
    return totale_tijd + kortste_verbinding.tijd

def verbindingen_vinden(huidig_station, totale_tijd, traject, verbindingen):
    #Zoek verbindingen en werk het traject bij totdat de tijdslimiet is bereikt
    while totale_tijd < 120:
        # Zoek mogelijke verbindingen
        mogelijke_verbindingen = vind_mogelijke_verbindingen(huidig_station, verbindingen)

        # Stop als er geen mogelijke verbindingen meer zijn
        if not mogelijke_verbindingen:
            break

        # Vind de kortste verbinding
        kortste_verbinding = vind_kortste_verbinding(mogelijke_verbindingen)

        # Controleer of de totale tijd binnen de limiet blijft
        if totale_tijd + kortste_verbinding.tijd > 120:
            break

        # Voeg de verbinding toe en werk de tijd bij
        totale_tijd = voeg_verbinding_toe_en_update_tijd(traject, kortste_verbinding, totale_tijd)

        # Update het huidige station
        huidig_station = update_huidig_station(huidig_station, kortste_verbinding)

        # Verwijder de gebruikte verbinding uit de lijst van verbindingen
        verbindingen.remove(kortste_verbinding)

    return traject

def bereken_totale_tijd(traject):
    # Bereken de totale reistijd van het traject.
    return sum(verbinding.tijd for verbinding in traject.traject)

tijd = 0
lijst = Verbindingen()
traject_1 = Traject(1)
traject_1 = verbindingen_vinden("Den Helder", tijd , traject_1, lijst.verbindingen)
print(traject_1.traject)
totale_tijd = bereken_totale_tijd(traject_1)
print(totale_tijd)