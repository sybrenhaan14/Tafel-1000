import csv
import random 

def kies_startstation (set_stations):
    return random.choice(list(set_stations))

class Stations:
    def __init__(self, naam):
        self.stations = self.laad_stations(naam)
        self.bezochte_stations = set()

    def laad_stations(self, naam):
        stations_list = set()
        with open(naam, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stations_list.add(row['station']) 
        return stations_list
    

    def is_bezocht(self, station):
        self.bezochte_stations.add(station)

    def eerder_bezocht(self, station):
        return station in self.bezochte_stations


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
    def __init__(self):
        # for aantal voeg traject toe en maak nieuw traject
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

class Opties:
    def __init__(self, stations_set, verbindingen):
        self.opties = {}
        self.verbindingen = verbindingen
        self.opties_zoeken(stations_set)
    
    def opties_zoeken(self, stations_set):
        for station in stations_set:
            self.opties[station] = []
            for v in self.verbindingen.verbindingen:
                if v.station1 == station:
                    self.opties[station].append(v.station2)
                if v.station2 == station:
                    self.opties[station].append(v.station1)

    def laad_opties(self, station):
        return self.opties.get(station, [])
    
    def kies_opties(self, station, bezochte_stations):
        keuzes = self.opties.get(station, [])
        # Filter stations die niet bezocht zijn
        ongebruikte_stations = [k for k in keuzes if k not in bezochte_stations]
        # Als er niet-bezochte stations zijn, kies daaruit
        if ongebruikte_stations:
            return random.choice(ongebruikte_stations)
        # zo niet kies een random station
        if keuzes:
            return random.choice(keuzes)

def verbindingen_vinden(huidig_station, opties, traject, station_set):
    totale_tijd = 0
    while totale_tijd < 120:
        # Gebruik opties om de eerste verbinding te kiezen
        station_set.is_bezocht(huidig_station)

        # Kies een volgende verbinding met voorkeur voor niet-bezochte stations
        volgende_station = opties.kies_opties(huidig_station, station_set.bezochte_stations)
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

    return traject

set_stations = Stations("../Data/StationsHolland.csv")
verbindingen_lijst = Verbindingen()
opties = Opties(set_stations.stations, verbindingen_lijst)

traject_1 = Traject(1)
start_station = kies_startstation(set_stations.stations)
traject_1 = verbindingen_vinden(start_station, opties, traject_1, set_stations)

print(f"Startstation: {start_station}")
print("Traject:", traject_1.traject)
print("Totale reistijd:", traject_1.bereken_totale_tijd())
print("Bezochte stations:", set_stations.bezochte_stations)