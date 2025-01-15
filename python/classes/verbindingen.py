import csv

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

    def zoek_verbinding(self, station1, station2):
        return next(
            (v for v in self.verbindingen 
             if (v.station1 == station1 and v.station2 == station2) or 
                (v.station2 == station1 and v.station1 == station2)),
            None
        )
