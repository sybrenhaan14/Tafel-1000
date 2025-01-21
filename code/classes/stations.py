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
        for verbinding in self.verbindingen.verbindingen:
            if verbinding.station1 in station_dict:
                station_dict[verbinding.station1].opties.append(station_dict[verbinding.station2])
            if verbinding.station2 in station_dict:
                station_dict[verbinding.station2].opties.append(station_dict[verbinding.station1])
    
    def geef_opties(self, station_naam):
        # geef de opties voor het opgegeven station
        for station in self.stations:
            if station.naam == station_naam:
                # for optie in station.opties:
                #     print(optie.naam)
                return station.opties

verbindingen = Verbindingen()
stations_obj = Stations('/mnt/c/Users/sybre/OneDrive/Documenten/Minor_prog/A_H/Tafel-1000/Data/StationsHolland.csv', verbindingen)

station_naam = 'Hoorn'
opties = stations_obj.geef_opties(station_naam)
