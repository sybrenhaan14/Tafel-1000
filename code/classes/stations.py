import csv
from verbindingen import *

class Station:
    def __init__(self, naam, y, x, opties): 
        self.naam = naam # naam station
        self.y = float(y) # Breedte graad
        self.x = float(x) # Lengte graad
        self.opties = opties # Verbonden stations

class Stations:
    def __init__(self, naam, verbindingen):
        # laad de stations in de lijst
        self.stations = self.laad_stations(naam)
        self.bezochte_stations = set() # set die bezochte stations bijhoudt
        self.verbindingen = verbindingen # de lijst van verbindingen tussen stations
        self.vul_opties_in() # vul de opties (verbonden stations) in voor elk station

    def laad_stations(self, naam):
        stations_list = [] # lijst waar alle stations wordt opgeslagen
        with open(naam, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Maak een nieuw Station voor elke rij in de CSV File met een lege lijst voor de opties
            for row in reader:
                stations_list.append(Station(row['station'], row['y'], row['x'], []))
        return stations_list
    
    def vul_opties_in(self):
        # maak een dict voor het snelle opzoeken van de stations op naam
        station_dict = {station.naam: station for station in self.stations}
        # loop door de verbindingen en voeg alle opties toe aan de list van opties
        for verbinding in self.verbindingen:
            if verbinding.station1 in station_dict:
                station_dict[verbinding.station1].opties.append(verbinding.station2)
            if verbinding.station2 in station_dict:
                station_dict[verbinding.station2].opties.append(verbinding.station1)
    
    def geef_opties(self, station_naam):
        # geef de opties voor het opgegeven station
        for station in self.stations:
            if station.naam == station_naam:
                return station.opties

    def is_bezocht(self, station):
        # voeg het station toe aan de set bezochte station
        self.bezochte_stations.add(station)

    def eerder_bezocht(self, station):
        # kijk of het station al is eerder bezocht of niet
        return station in self.bezochte_stations