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
    
    def kies_opties(self, station, bezochte_stations, gereden_verbindingen):
        keuzes = self.opties.get(station, [])
        # Filter verbindingen die zijn gereden
        ongebruikte_stations = [k for k in keuzes if k not in bezochte_stations]
        if ongebruikte_stations:
            keuze = random.choice(ongebruikte_stations)
            # check = {keuze, station}
            # gereden_verbindingen.add(check)
            return keuze
        else:
            keuze = random.choice(keuzes)
            return keuze

