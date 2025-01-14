import csv
import random 

def kies_startstation (stations):
    stations = laad_stations("../Data/StationsHolland.csv")
    random_start_station = random.choice(list(stations))
    return random_start_station

def laad_stations(naam):
    stations = set()
    with open(naam, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.add(row['station']) 
    return stations

class Verbinding:
    def __init__(self, station1, station2, tijd):
        self.station1 = station1
        self.station2 = station2
        self.tijd = int(tijd)

    def __repr__(self):
        return f"{self.station1} -> {self.station2} ({self.tijd} min)"

class Verbindingen:
    def __init__(self):
        self.verbindingen = []
        self.laad_verbindingen('../Data/ConnectiesHolland.csv')

    def laad_verbindingen(self, bestand):
        # Lees de verbindingen uit een CSV bestand en sla ze op als Verbinding objecten
        with open(bestand, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                verbinding = Verbinding(row['station1'], row['station2'], row['distance'])
                self.verbindingen.append(verbinding)


class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []

    def voeg_verbinding_toe(self, verbinding):
        self.traject.append(verbinding)

    def bereken_totale_tijd(self):
        return sum(verbinding.tijd for verbinding in self.traject)

class Netwerken:
    def __init__(self, netwerk):
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

# class Verbindingzoeker:
#     def __init__(self, verbindingen):
#         self.verbindingen = verbindingen
    
#     def vind_mogelijke_verbindingen(huidig_station, verbindingen):
#         #Zoek verbindingen die aansluiten bij het huidige station
#         return [
#          v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
#         ]
#     def vind_kortste_verbinding(mogelijke_verbindingen):
#         #Vind de verbinding met de kortste reistijd
#         return min(mogelijke_verbindingen, key=lambda v: v.tijd)
    
#     def update_huidig_station(huidig_station, kortste_verbinding):
#         #Werk het huidige station bij op basis van de verbinding
#         return kortste_verbinding.station2 if kortste_verbinding.station1 == huidig_station else kortste_verbinding.station1
    
#     def voeg_verbinding_toe_en_update_tijd(traject, kortste_verbinding, totale_tijd):
#         #Voeg de verbinding toe aan het traject en werk de totale tijd bij
#         traject.voeg_verbinding_toe(kortste_verbinding)
#         return totale_tijd + kortste_verbinding.tijd

class Opties:
    def __init__(self, stations, verbindingen):
        self.opties = {}
        self.stations = stations
        self.verbindingen = verbindingen
        self.opties_zoeken()
    
    def opties_zoeken(self):
        for station in self.stations:
            self.opties[station] = []
            for v in self.verbindingen.verbindingen:
                if v.station1 == station:
                    self.opties[station].append(v.station2)
                if v.station2 == station:
                    self.opties[station].append(v.station1)

    def laad_opties(self, station):
        return self.opties.get(station, [])
    
    def kies_opties(self, station):
        keuze = self.opties.get(station, [])
        return keuze[0]

def verbindingen_vinden(huidig_station, opties, traject):
    totale_tijd = 0
    while totale_tijd < 120:
        # Gebruik opties om de eerste verbinding te kiezen
        volgende_station = opties.kies_opties(huidig_station)
        if not volgende_station:
            break  # Geen verdere verbindingen mogelijk

        # Zoek de verbinding tussen het huidige en volgende station
        verbinding = next(
            (v for v in opties.verbindingen.verbindingen
             if (v.station1 == huidig_station and v.station2 == volgende_station) or
                (v.station2 == huidig_station and v.station1 == volgende_station)),
            None
        )
        if not verbinding:
            break

        # Controleer of de tijdslimiet niet wordt overschreden
        if totale_tijd + verbinding.tijd > 120:
            break

        # Voeg de verbinding toe en werk de tijd en het huidige station bij
        traject.voeg_verbinding_toe(verbinding)
        totale_tijd += verbinding.tijd
        huidig_station = volgende_station

        # Verwijder de gebruikte verbinding uit de lijst
        opties.verbindingen.verbindingen.remove(verbinding)

    return traject

lijst_stations = laad_stations("../Data/StationsHolland.csv")
verbindingen_lijst = Verbindingen()
opties = Opties(lijst_stations, verbindingen_lijst)

traject_1 = Traject(1)
start_station = kies_startstation(lijst_stations)
traject_1 = verbindingen_vinden(start_station, opties, traject_1)

print(f"Startstation: {start_station}")
print("Traject:", traject_1.traject)
print("Totale reistijd:", traject_1.bereken_totale_tijd())