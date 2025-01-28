from verbindingen import *
from stations import *

# def kies_opties_greedy(opties, huidige_station_naam, gereden_verbindingen):
#     for optie in opties:
#         # Controleer of de verbinding tussen de stations al gereden is
#         if (huidige_station_naam, optie.naam) not in gereden_verbindingen and \
#            (optie.naam, huidige_station_naam) not in gereden_verbindingen:
#             return optie  # Retourneer het geselecteerde station
#     return opties[0]

def kies_opties_greedy(opties, huidige_station_naam, gereden_verbindingen):
    for optie in opties:
        if (huidige_station_naam, optie.naam) not in gereden_verbindingen and \
           (optie.naam, huidige_station_naam) not in gereden_verbindingen:
            print(f"Gekozen optie: {huidige_station_naam} -> {optie.naam}")
            return optie
    print(f"Geen opties meer beschikbaar vanuit {huidige_station_naam}")
    return opties[0]
