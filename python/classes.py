import csv

class Station():
    def __init__(self, naam, latitude, longitude):
        self.naam = naam
        self.latitude = float(latitude)
        self.longitude = float(longitude)

stations = []

with open('../csv_files/StationsHolland.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        station = Station(row['naam'], row['latitude'], row['longitude'])
        stations.append(station)

class Verbinding:

    def __init__(self, station1, station2, tijd):
        self.station1 = station1
        self.station2 = station2
        self.tijd = tijd

verbindingen = [
    Verbinding("Alkmaar","Hoorn",24),
    Verbinding("Alkmaar", "Den Helder", 36),
    Verbinding("Amsterdam Amstel", "Amsterdam Zuid", 10),
    Verbinding("Amsterdam Amstel", "Amsterdam Centraal", 8),
    Verbinding("Amsterdam Centraal", "Amsterdam Sloterdijk", 6),
    Verbinding("Amsterdam Sloterdijk", "Haarlem", 11),
    Verbinding("Amsterdam Sloterdijk", "Zaandam", 6),
    Verbinding("Amsterdam Zuid","Amsterdam Sloterdijk", 16),
    Verbinding("Amsterdam Zuid", "Schiphol Airport", 6),
    Verbinding("Beverwijk", "Castricum", 13),
    Verbinding("Castricum", "Alkmaar", 9),
    Verbinding("Delft", "Den Haag Centraal", 13),
    Verbinding("Den Haag Centraal", "Gouda", 18),
    Verbinding("Den Haag Centraal", "Leiden Centraal", 12),
    Verbinding("Dordrecht", "Rotterdam Centraal", 17),
    Verbinding("Gouda", "Alphen a/d Rijn", 19),
    Verbinding("Haarlem", "Beverwijk", 16),
    Verbinding("Heemstede-Aerdenhout", "Haarlem", 6),
    Verbinding("Leiden Centraal", "Heemstede-Aerdenhout", 13),
    Verbinding("Leiden Centraal", "Alphen a/d Rijn", 14),
    Verbinding("Leiden Centraal", "Schiphol Airport", 15),
    Verbinding("Rotterdam Alexander", "Gouda", 10),
    Verbinding("Rotterdam Centraal", "Schiedam Centrum", 5),
    Verbinding("Rotterdam Centraal","Rotterdam Alexander", 8),
    Verbinding("Schiedam Centrum", "Delft", 7),
    Verbinding("Zaandam", "Castricum", 12),
    Verbinding("Zaandam", "Beverwijk", 25),
    Verbinding("Zaandam", "Hoorn", 26)
]

class Traject:
    def __init__(self, traject_id, totale_tijd):
        self.traject_id = traject_id
        self.totale_tijd = totale_tijd
        self.trein = []

    def voeg_verbinding_toe(self, verbinding):
        self.trein.append(verbinding)

    def bereken_totale_tijd(self):
        totale_tijd = sum(verbinding.tijd for verbinding in self.trein)
        return totale_tijd


