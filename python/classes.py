import csv

class Station():
    def __init__(self, naam, latitude, longitude):
        self.naam = naam
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def laad_stations(self):
        stations = []
        with open('../csv_files/StationsHolland.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                station = Station(row['naam'], row['latitude'], row['longitude'])
                stations.append(station)
        return stations

class Verbinding:

    def __init__(self, station1, station2, tijd):
        self.station1 = station1
        self.station2 = station2
        self.tijd = int(tijd)

    def laad_verbindingen(self):
        verbindingen = []
        with open('../csv_files/ConnectiesHolland.csv', 'r', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    verbinding = Verbinding(row['station1'], row['station2'], row['tijd'])
                    verbindingen.append(verbinding)
        return verbindingen

class Traject:
    def __init__(self, traject_id, totale_tijd):
        self.traject_id = traject_id
        self.totale_tijd = totale_tijd
        self.traject = []

    def voeg_verbinding_toe(self, verbinding):
        self.traject.append(verbinding)

    def __repr__(self):
        verbindingen_str = "\n".join([f"{v.station1} ↔ {v.station2} ({v.tijd} min)" for v in self.traject])
        return f"Traject {self.traject_id}:\n{verbindingen_str}\nTotale tijd: {self.totale_tijd} minuten"

class Netwerken:
    def __init__(self, netwerk):
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)
