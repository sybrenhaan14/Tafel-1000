import random
from netwerk import *
from opties import *
from traject import *
from verbindingen import *
from stations import *


class Netwerken:
    def __init__(self, stations_set, verbindingen_lijst, max_trajecten=7, tijdslimiet=120):
        self.stations_set = stations_set
        self.verbindingen_lijst = verbindingen_lijst
        self.max_trajecten = max_trajecten
        self.tijdslimiet = tijdslimiet
        self.netwerk = Netwerk()

    def genereer_trajecten(self, stations, verbindingen):
        netwerk = Netwerk()
        trajecten = 0

        while not netwerk.alle_verbindingen_bereikt(verbindingen):
            traject = Traject(trajecten + 1)
            start_station = self.kies_startstation()
                    # Voeg verbindingen toe aan het traject
            huidig_station = start_station
            bereden_verbindingen = set()

            # Voeg verbindingen toe tot het traject de tijdslimiet overschrijdt of alle verbindingen zijn bereden
            self.voeg_verbindingen_toe(huidig_station, traject, bereden_verbindingen)

            # Voeg het traject toe aan het netwerk
            netwerk.voeg_traject_toe(traject)
            return self.netwerk

    def kies_startstation(self):
        return random.choice(list(self.stations_set.stations))

    def voeg_verbindingen_toe(self, huidig_station, traject, bereden_verbindingen):
        
        opties = Opties(self.stations_set.stations, self.verbindingen_lijst)
        totale_tijd = 0

        while totale_tijd < self.tijdslimiet:
            volgende_verbinding = opties.kies_opties(huidig_station)
            bereden_verbindingen.add(volgende_verbinding)
            
            if volgende_verbinding in bereden_verbindingen:
                break

            
            verbinding = self.verbindingen_lijst.zoek_verbinding(huidig_station, volgende_verbinding)
            if verbinding:
                if totale_tijd + verbinding.tijd > self.tijdslimiet:
                    break  
                traject.voeg_verbinding_toe(verbinding)
                totale_tijd += verbinding.tijd
                huidig_station = volgende_verbinding
            else:
                break

    def controleer_niet_bezochte_stations(self):
        
        bezochte_stations = set()
        for traject in self.netwerk.netwerk:
            for verbinding in traject.traject:
                bezochte_stations.add(verbinding.station1)
                bezochte_stations.add(verbinding.station2)

        niet_bezochte_stations = self.stations_set.stations - bezochte_stations
        return niet_bezochte_stations