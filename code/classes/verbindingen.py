import csv

class Verbinding:
    def __init__(self, station1, station2, tijd, id):
        self.station1 = station1
        self.station2 = station2
        self.tijd = int(tijd)
        self.id = id # individuele id voor elke verbinding

    def __repr__(self):
        # De string die de verbinding beschrijft
        return f"Verbinding({self.station1} <-> {self.station2}, Tijd: {self.tijd})"

class Verbindingen:
    def __init__(self, pad):
        # maakt een lijst voor de verbindingen
        self.verbindingen = []
        # maakt een set voor de gereden verbindingen
        self.gereden_verbindingen = set()
        # laad de verbindingen in de lijst
        self.laad_verbindingen(pad)

    def laad_verbindingen(self, bestand):
        # Lees de verbindingen uit een CSV bestand en sla ze op als Verbinding objecten
        id = 0
        with open(bestand, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id += 1
                verbinding = Verbinding(row['station1'], row['station2'], row['distance'], id)
                self.verbindingen.append(verbinding)

    def zoek_verbinding(self, station1, station2):
        # kijkt naar of er een echte verbinding is tussen de twee stations
        return next(
            (v for v in self.verbindingen 
             if (v.station1 == station1 and v.station2 == station2) or 
                (v.station2 == station1 and v.station1 == station2)),
            None
        )
