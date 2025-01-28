import random
from abc import ABC, abstractmethod

class Algoritme(ABC):
    def __init__(self, stations_lijst, verbindingen_lijst):
        self.stations_lijst = stations_lijst
        self.verbindingen_lijst = verbindingen_lijst

    @abstractmethod
    def kies_startstation(self, bezochte_stations):
        # Selecteert een startstation op basis van het algoritme
        pass

    @abstractmethod
    def kies_volgende_station(self, huidig_station, opties_huidig_station, gereden_verbindingen):
        # Selecteert het volgende station op basis van het algoritme
        pass


class Random(Algoritme):    
    def kies_startstation(self, bezochte_stations):
        # Kiest willekeurig een station als start
        return random.choice(self.stations_lijst.stations)
    
    def kies_volgende_station(self, huidig_station, opties_huidig_station, gereden_verbindingen):
        # Kiest willekeurig een volgend station
        return random.choice(opties_huidig_station)


class Greedy(Algoritme):
    def kies_startstation(self, bezochte_stations):
        # Kiest een station dat nog niet bezocht is en anders kiest random
        niet_bezocht = [station for station in self.stations_lijst.stations if station not in bezochte_stations]
        if niet_bezocht:
            return random.choice(niet_bezocht)
        else:
            return random.choice(self.stations_lijst.stations)
    
    def kies_volgende_station(self, huidig_station, opties_huidig_station, gereden_verbindingen):
        # Kiest het station met de kortste verbinding die nog niet is bereden
        for optie in opties_huidig_station:
            # Controleer of de verbinding tussen de stations al gereden is
            if (huidig_station.naam, optie.naam) not in gereden_verbindingen and \
               (optie.naam, huidig_station.naam) not in gereden_verbindingen:
                return optie  # Retourneer het geselecteerde station
        # Fallback als alle verbindingen zijn bereden
        return random.choice(opties_huidig_station)
