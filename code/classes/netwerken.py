import random
from random import *
from traject import *
from stations import *
from random import *

class Netwerk:
    def __init__(self):
        # for aantal voeg traject toe en maak nieuw traject
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

    def alle_verbindingen_bereikt(self, verbindingen):
        return len(verbindingen.bereden_verbindingen) == len(verbindingen.verbindingen)

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

        while trajecten < self.max_trajecten:
            traject = Traject(trajecten + 1)
            start_station = self.kies_startstation(bezochte_stations)
            self.stations_set.eerder_bezocht(start_station)  
            self.voeg_verbindingen_toe(start_station, traject, gereden_verbindingen)


            self.netwerk.voeg_traject_toe(traject)
            trajecten += 1

        return self.netwerk

    def kies_startstation(self, bezochte_stations):

        overgebleven_stations = self.stations_set.stations - bezochte_stations
        return random.choice(list(overgebleven_stations))

    def voeg_verbindingen_toe(self, huidig_station, traject, gereden_verbindingen):
        
        opties = Opties(self.stations_set.stations, self.verbindingen_lijst)
        totale_tijd = 0

        while totale_tijd < self.tijdslimiet:

            volgende_station = opties.kies_opties(huidig_station, gereden_verbindingen)
            
            verbinding = self.verbindingen_lijst.zoek_verbinding(huidig_station, volgende_station)
            if verbinding:
                if totale_tijd + verbinding.tijd > self.tijdslimiet:
                    break  
                traject.voeg_verbinding_toe(verbinding)
                totale_tijd += verbinding.tijd
                huidig_station = volgende_station
            else:
                break

    def controleer_niet_bezochte_verbindingen(self):
        # Houd een set bij van bezochte verbindingen
        bezochte_verbindingen = set()
        for traject in self.netwerk.netwerk:
            for verbinding in traject.traject:
                # Voeg elke bezochte verbinding toe als een tuple (station1, station2)
                bezochte_verbindingen.add((verbinding.station1, verbinding.station2))
                bezochte_verbindingen.add((verbinding.station2, verbinding.station1))  # Beide richtingen

        # Maak een set van alle verbindingen
        alle_verbindingen = set(
            (v.station1, v.station2) for v in self.verbindingen_lijst.verbindingen
        )

        # Bereken de niet-bezochte verbindingen
        niet_bezochte_verbindingen = alle_verbindingen - bezochte_verbindingen

        return niet_bezochte_verbindingen
    
class Score:
    def __init__(self, netwerk):
        self.netwerk = netwerk

    def bereken_score(self):
        aantal_bereden_verbindingen = len(self.netwerk.netwerk)
        aantal_trajecten = len(self.netwerk.netwerk)
        Min = sum(verbinding.tijd for traject in self.netwerk.netwerk for verbinding in traject.traject)

        score = (aantal_bereden_verbindingen / 28 ) * 10000 - (aantal_trajecten * 100 + Min)

        return score
