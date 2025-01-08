class station():
    def __init__(self, naam, latitude, longitude):
        self.naam = naam
        self.latitude = latitude
        self.longitude = longitude

stations = [
    Station("Alkmaar", 52.63777924, 4.739722252),
    Station("Alphen a/d Rijn", 52.12444305, 4.657777786),
    Station("Amsterdam Amstel", 52.34666824, 4.917778015),
    Station("Amsterdam Centraal", 52.37888718, 4.900277615),
    Station("Amsterdam Sloterdijk", 52.38888931, 4.837777615),
    Station("Amsterdam Zuid", 52.338889, 4.872356),
    Station("Beverwijk", 52.47833252, 4.656666756),
    Station("Castricum", 52.54583359, 4.658611298),
    Station("Delft", 52.00666809, 4.356389046),
    Station("Den Haag Centraal", 52.08027649, 4.324999809),
    Station("Den Helder", 52.95527649, 4.761111259),
    Station("Dordrecht", 51.80722046, 4.66833353),
    Station("Gouda", 52.01750183, 4.704444408),
    Station("Haarlem", 52.38777924, 4.638333321),
    Station("Heemstede-Aerdenhout", 52.35916519, 4.606666565),
    Station("Hoorn", 52.64472198, 5.055555344),
    Station("Leiden Centraal", 52.16611099, 4.481666565),
    Station("Rotterdam Alexander", 51.95194626, 4.553611279),
    Station("Rotterdam Centraal", 51.92499924, 4.46888876),
    Station("Schiedam Centrum", 51.92124381, 4.408993721),
    Station("Schiphol Airport", 52.30944443, 4.761944294),
    Station("Zaandam", 52.43888855, 4.813611031)
]


class verbinding:

    def __init__(self, station1, station2, tijd, verbinding_id):
        self.station1 = station1
        self.station2 = station2
        self.tijd = tijd
        self.verbinding_id = verbinding_id

verbindingen = [
    verbinding("Alkmaar","Hoorn",24, 100),
    verbinding("Alkmaar", "Den Helder", 36, 101),
    verbinding("Amsterdam Amstel", "Amsterdam Zuid", 10, 102),
    verbinding("Amsterdam Amstel", "Amsterdam Centraal", 8, 103),
    verbinding("Amsterdam Centraal", "Amsterdam Sloterdijk", 6, 104),
    verbinding("Amsterdam Sloterdijk", "Haarlem", 11, 105),
    verbinding("Amsterdam Sloterdijk", "Zaandam", 6, 106),
    verbinding("Amsterdam Zuid","Amsterdam Sloterdijk", 16, 107),
    verbinding("Amsterdam Zuid", "Schiphol Airport", 6, 108),
    verbinding("Beverwijk", "Castricum", 13, 109),
    verbinding("Castricum", "Alkmaar", 9, 110),
    verbinding("Delft", "Den Haag Centraal", 13, 111),
    verbinding("Den Haag Centraal", "Gouda", 18, 112),
    verbinding("Den Haag Centraal", "Leiden Centraal", 12, 113),
    verbinding("Dordrecht", "Rotterdam Centraal", 17, 114),
    verbinding("Gouda", "Alphen a/d Rijn", 19, 115),
    verbinding("Haarlem", "Beverwijk", 16, 116),
    verbinding("Heemstede-Aerdenhout", "Haarlem", 6, 117),
    verbinding("Leiden Centraal", "Heemstede-Aerdenhout", 13, 118),
    verbinding("Leiden Centraal", "Alphen a/d Rijn", 14, 119),
    verbinding("Leiden Centraal", "Schiphol Airport", 15, 120),
    verbinding("Rotterdam Alexander", "Gouda", 10, 121),
    verbinding("Rotterdam Centraal", "Schiedam Centrum", 5, 122),
    verbinding("Rotterdam Centraal","Rotterdam Alexander", 8, 123),
    verbinding("Schiedam Centrum", "Delft", 7, 124),
    verbinding("Zaandam", "Castricum", 12, 125),
    verbinding("Zaandam", "Beverwijk", 25, 126),
    verbinding("Zaandam", "Hoorn", 26, 127)
]

class traject:
    def __init__(self, traject_id, totale_tijd):
        self.traject_id = traject_id
        self.totale_tijd = totale_tijd
        self.trein = []

    def voeg_verbinding_toe(self, verbinding):
        self.trein.append(verbinding)

    def bereken_totale_tijd(self):
        totale_tijd = sum(verbinding.tijd for verbinding in self.trein)
        return totale_tijd

# Startpunt en initialisatie
huidig_station = "Alkmaar"
totale_tijd = 0
gekozen_verbindingen = []

while totale_tijd < 120:
    # Vind verbindingen met huidig station
    mogelijke_verbindingen = [
        v for v in verbindingen if v.station1 == huidig_station or v.station2 == huidig_station
    ]

    # Als er geen mogelijke verbindingen meer zijn, stop de loop
    if not mogelijke_verbindingen:
        break

    # Vind verbinding met de kortste tijd
    kortste_verbinding = min(mogelijke_verbindingen, key=lambda v: v.tijd)

    # Controleer of toevoegen van verbinding binnen limiet blijft
    if totale_tijd + kortste_verbinding.tijd > 120:
        break

    # Voeg verbinding toe en update totale tijd
    gekozen_verbindingen.append(kortste_verbinding)
    totale_tijd += kortste_verbinding.tijd

    # Update huidig station naar het andere station in de gekozen verbinding
    if kortste_verbinding.station1 == huidig_station:
        huidig_station = kortste_verbinding.station2
    else:
        huidig_station = kortste_verbinding.station1

    # Verwijder de gebruikte verbinding
    verbindingen.remove(kortste_verbinding)

# Print het resultaat
print(f"Totale tijd: {totale_tijd} minuten")
print("Gekozen verbindingen:")
for v in gekozen_verbindingen:
    print(f"{v.station1} -> {v.station2} ({v.tijd} min)")