import random
from netwerk import *
from opties import *
from traject import *

class Netwerken:
    def __init__(self, stations_set, verbindingen_lijst, max_trajecten=7, tijdslimiet=120):
        self.stations_set = stations_set
        self.verbindingen_lijst = verbindingen_lijst
        self.max_trajecten = max_trajecten
        self.tijdslimiet = tijdslimiet
        self.netwerk = Netwerk()

    def genereer_trajecten(self):
        
        bezochte_stations = set() 
        gereden_verbindingen = set()
        trajecten = 0

        while trajecten < self.max_trajecten and len(bezochte_stations) < len(self.stations_set.stations):
            traject = Traject(trajecten + 1)
            start_station = self.kies_startstation(bezochte_stations)
            self.stations_set.eerder_bezocht(start_station)  
            self.voeg_verbindingen_toe(start_station, traject, gereden_verbindingen, bezochte_stations)

            
            for v in traject.traject:
                bezochte_stations.add(v.station1)
                bezochte_stations.add(v.station2)

            self.netwerk.voeg_traject_toe(traject)
            trajecten += 1

        return self.netwerk

    def kies_startstation(self, bezochte_stations):

        overgebleven_stations = self.stations_set.stations - bezochte_stations
        return random.choice(list(overgebleven_stations))

    def voeg_verbindingen_toe(self, huidig_station, traject, gereden_verbindingen, bezochte_stations):
        
        opties = Opties(self.stations_set.stations, self.verbindingen_lijst)
        totale_tijd = 0

        while totale_tijd < self.tijdslimiet:

            bezochte_stations.add(huidig_station)
            volgende_station = opties.kies_opties(huidig_station, bezochte_stations, gereden_verbindingen)
            
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