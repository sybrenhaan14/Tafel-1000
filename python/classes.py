import csv

def laad_stations(self, naam):
    stations = []
    with open(naam, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row['station'])
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
        self.laad_verbindingen('../csv_files/ConnectiesHolland.csv')

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

class Netwerken:
    def __init__(self, netwerk):
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

class Verbindingzoeker:
    def __init__(self, verbindingen):
        self.verbindingen = verbindingen
    
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

class Opties:
    def _init_(self, stations, verbindingen, opties):
        self.opties = {}
        stations = laad_staions("../Data/StationsHolland.csv")
        verbindingen = Verbindingen()
        self.opties_zoeken

    def opties_zoeken(self):
        for station in self.stations:
            self.opties[station] = []
            for v in self.verbindingen.verbindingen:
                if v.station1 == station or v.station2 == station:
                    self.opties[station] = v

    def laad_opties(self, station):
        return self.opties.get(station, [])

