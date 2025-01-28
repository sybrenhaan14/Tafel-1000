from verbindingen import *
from stations import *

def kies_opties_greedy(opties, huidige_station_naam, gereden_verbindingen):
    for optie in opties:
        # Controleer of de verbinding tussen de stations al gereden is
        if (huidige_station_naam, optie.naam) not in gereden_verbindingen and \
           (optie.naam, huidige_station_naam) not in gereden_verbindingen:
            return optie  # Retourneer het geselecteerde station
    return opties[0]

#def kies_opties_greedy(opties, huidige_station_naam, gereden_verbindingen):
#    for optie in opties:
#        # Controleer of de verbinding tussen de stations al gereden is
#        if (huidige_station_naam, optie.naam) not in gereden_verbindingen and \
#           (optie.naam, huidige_station_naam) not in gereden_verbindingen:
#            print(f"Gekozen optie: {huidige_station_naam} -> {optie.naam}")
#            return optie
#    print(f"Geen opties meer beschikbaar vanuit {huidige_station_naam}")
#    return opties[0]

def kies_opties_greedy(opties, huidige_station_naam, gereden_verbindingen, max_herhalingen):
    """
    Kies een optie op basis van het greedy algoritme, met respect voor de limiet van max_herhalingen.
    """
    for optie in opties:
        verbinding = (huidige_station_naam, optie.naam)
        # Controleer of de verbinding niet de maximale herhalingen heeft overschreden
        if gereden_verbindingen.get(verbinding, 0) < max_herhalingen:
            # Bijwerken van de verbindingen
            gereden_verbindingen[verbinding] = gereden_verbindingen.get(verbinding, 0) + 1
            gereden_verbindingen[(optie.naam, huidige_station_naam)] = gereden_verbindingen.get((optie.naam, huidige_station_naam), 0) + 1
            print(f"Gekozen optie: {huidige_station_naam} -> {optie.naam}")
            return optie
    print(f"Geen opties meer beschikbaar vanuit {huidige_station_naam}")
    return None
