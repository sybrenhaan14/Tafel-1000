

# Startpunt en initialisatie
huidig_station = "Alkmaar"
totale_tijd = 0
gekozen_verbindingen = []

while totale_tijd < 120:
    # Vind verbindingen met huidig station
    mogelijke_verbindingen = [
        v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
    ]

    # Als er geen mogelijke verbindingen meer zijn, stop de loop
    if not mogelijke_verbindingen:
        break

    # Vind verbinding met de kortste tijd
    kortste_verbinding = min(mogelijke_verbindingen, key=lambda v: v.tijd)

    # Controleer of toevoegen van verbinding binnen limiet blijft
    if totale_tijd + kortste_verbinding.tijd > 120:
        break

    # Voeg verbinding toe en update totale tijd
    gekozen_verbindingen.append(kortste_verbinding)
    totale_tijd += kortste_verbinding.tijd

    # Update huidig station naar het andere station in de gekozen verbinding
    if kortste_verbinding.station1 == huidig_station:
        huidig_station = kortste_verbinding.station2
    else:
        huidig_station = kortste_verbinding.station1

    # Verwijder de gebruikte verbinding
    verbindingen.remove(kortste_verbinding)