import csv
import random 

class Stations:
    def __init__(self, naam):
        self.stations = self.laad_stations(naam)
        self.bezochte_stations = set()

    def laad_stations(self, naam):
        stations_list = set()
        with open(naam, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stations_list.add(row['station']) 
        return stations_list
    
    def kies_startstation(set_stations):
        return random.choice(list(set_stations))

    def is_bezocht(self, station):
        self.bezochte_stations.add(station)

    def eerder_bezocht(self, station):
        return station in self.bezochte_stations