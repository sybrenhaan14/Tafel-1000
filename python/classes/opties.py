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

    def laad_opties(self, station):
        return self.opties.get(station, [])
    
    def kies_opties(self, station):
        while(True):
            keuzes = self.opties.get(station, [])
            keuze = random.choice(keuzes)
            gekozen_verbinding = self.verbindingen.zoek_verbinding(station, keuze)
            if not gekozen_verbinding in self.verbindingen.bereden_verbindingen:
                return gekozen_verbinding

