import random
from verbindingen import *

class Opties:
    def __init__(self, stations_set, verbindingen):
        self.opties = {}
        self.verbindingen = verbindingen
        self.opties_zoeken(stations_set)
    
    def opties_zoeken(self, stations_set):
        for station in stations_set:
            self.opties[station] = []
            for v in self.verbindingen.verbindingen:
                if v.station1 == station:
                    self.opties[station].append(v.station2)
                if v.station2 == station:
                    self.opties[station].append(v.station1)
    
    def kies_opties_random(self, station, gereden_verbindingen):
        keuzes = self.opties.get(station, [])
        keuze = random.choice(keuzes)
        return keuze
