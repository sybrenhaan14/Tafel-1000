import csv
import random 
from verbindingen import *

class Station:
    def __init__(self, naam, y, x, opties):
        self.naam = naam
        self.y = float(y)
        self.x = float(x)
        self.opties = opties

class Stations:
    def __init__(self, naam, verbindingen):
        self.stations = self.laad_stations(naam)
        self.bezochte_stations = set()
        self.verbindingen = verbindingen
        self.vul_opties_in()

    def laad_stations(self, naam):
        stations_list = []
        with open(naam, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stations_list.append(Station(row['station'], row['y'], row['x']))
        return stations_list
    
    def vul_opties_in(self):
        station_dict = {station.naam: station for station in self._stations}
        for verbinding in self.verbindingen:
            if verbinding.station1 in station_dict:
                station_dict[verbinding.station1].opties.append(verbinding.station2)
            if verbinding.station2 in station_dict:
                station_dict[verbinding.station2].opties.append(verbinding.station1)
    
    def geef_opties(self, station_naam):
        for station in self.stations:
            if station.naam == station_naam:
                return station.opties

    def is_bezocht(self, station):
        self.bezochte_stations.add(station)

    def eerder_bezocht(self, station):
        return station in self.bezochte_stations