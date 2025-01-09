import csv

def laad_stations(self):
    stations = []
    with open('../csv_files/StationsHolland.csv', 'r', encoding='utf-8') as csvfile:
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
        with open('../csv_files/ConnectiesHolland.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                verbinding = Verbinding(row['station1'], row['station2'], row['distance'])
                self.verbindingen.append(verbinding)

class Traject:
    def __init__(self, traject_id, totale_tijd):
        self.traject_id = traject_id
        self.totale_tijd = totale_tijd
        self.traject = []

    def voeg_verbinding_toe(self, verbinding):
        self.traject.append(verbinding)

class Netwerken:
    def __init__(self, netwerk):
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)
