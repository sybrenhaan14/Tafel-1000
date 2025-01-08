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