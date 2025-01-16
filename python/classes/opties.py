import random

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
    
    def kies_opties(self, station, bezochte_stations):
        keuzes = self.opties.get(station, [])
        # Filter stations die niet bezocht zijn
        ongebruikte_stations = [k for k in keuzes if k not in bezochte_stations]
        # Als er niet-bezochte stations zijn, kies daaruit
        if ongebruikte_stations:
            return random.choice(ongebruikte_stations)
        # zo niet kies een random station
        if keuzes:
            return random.choice(keuzes)
        
    def volgende_verbinding(self, station, bereden_verbindingen):
        keuzes = self.opties.get(station, [])
        # Filter stations die niet bezocht zijn
        ongebruikte_verbinding = [k for k in keuzes if k not in bereden_verbindingen]
        # Als er niet-bezochte stations zijn, kies daaruit
        if ongebruikte_verbinding:
            return random.choice(ongebruikte_verbinding)
        # zo niet kies een random station
        if keuzes:
            return random.choice(keuzes)
