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
        # Voeg meer verbindingen toe totdat het traject vol is
            while not traject.is_volledig():
                volgende_verbinding = Opties.volgende_verbinding(huidig_station, bereden_verbindingen)
                if volgende_verbinding:
                    traject.voeg_verbinding_toe(volgende_verbinding, verbindingen)
                netwerk.voeg_traject_toe(traject)
                trajecten += 1

            return self.netwerk

    def kies_startstation(self):
        return random.choice(list(self.stations_set.stations))

    def voeg_verbindingen_toe(self, huidig_station, traject, bezochte_stations):
        
        opties = Opties(self.stations_set.stations, self.verbindingen_lijst)
        totale_tijd = 0

        while totale_tijd < self.tijdslimiet:
            if huidig_station in bezochte_stations:
                break

            bezochte_stations.add(huidig_station)
            volgende_station = opties.kies_opties(huidig_station, bezochte_stations)

            
            if volgende_station in bezochte_stations:
                break

            
            verbinding = self.verbindingen_lijst.zoek_verbinding(huidig_station, volgende_station)
            if verbinding:
                if totale_tijd + verbinding.tijd > self.tijdslimiet:
                    break  
                traject.voeg_verbinding_toe(verbinding)
                totale_tijd += verbinding.tijd
                huidig_station = volgende_station
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