import random
from random_algo import *
from traject import *
from stations import *
from Greedy import *

# Klasse om netwerk van trajecten te beheren
class Netwerk:
    def __init__(self):
        # Lijst van trajecten die deel uitmaken van het netwerk
        self.netwerk = []
        self.gereden_verbindingen = set()
        self.bezochte_stations = set()

    # Voegt traject toe aan netwerk
    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

    # Checkt of alle verbindingen bereden zijn
    def alle_verbindingen_bereikt(self, verbindingen):
        return len(verbindingen.bereden_verbindingen) == len(verbindingen.verbindingen)

# Klasse om trajecten te generern
class Netwerken:
    def __init__(self, stations_set, verbindingen_lijst, regio):
        self.stations_set = stations_set
        self.verbindingen_lijst = verbindingen_lijst
        self.netwerk = Netwerk()

        if regio == 'H':
            self.tijdslimiet = 120
            self.max_trajecten = 7
        
        if regio == 'N':
            self.max_tijdslimiet = 180
            self.max_trajecten = 20

    # Genereert een netwerk met trajecten
    def genereer_trajecten(self, algo):
        
        trajecten = 0

        while trajecten < self.max_trajecten:
            traject = Traject(trajecten + 1)
            start_station = self.kies_startstation(algo)
            self.voeg_verbindingen_toe(start_station, traject, algo)

            # Voegt traject toe aan netwerk
            self.netwerk.voeg_traject_toe(traject)
            trajecten += 1 # Verhoogt het aantal trajecten met 1

        return self.netwerk

    # Kiest een station dat nog niet eerder is bezocht
    def kies_startstation(self, algo):
        if algo == 'G':
            niet_bezocht = [item for item in self.stations_set.stations if item not in self.netwerk.bezochte_stations]
            if niet_bezocht:
                return random.choice(niet_bezocht)
            else:
                return random.choice(self.stations_set.stations)
        if algo == 'R':
            return random.choice(self.stations_set.stations)

    # Voegt verbindingen toe aan traject todat de tijdslimiet is bereikt
    def voeg_verbindingen_toe(self, huidig_station, traject, algo):
        

        totale_tijd = 0 #houd te tijd bij

        while totale_tijd < self.tijdslimiet:
           
            traject.bezochte_stations.append(huidig_station.naam)
            self.netwerk.bezochte_stations.add(huidig_station.naam)
            # Kiest volgend station en voegt verbinding toe 
            opties_huidig_station = self.stations_set.geef_opties(huidig_station.naam)
            if algo == 'R':
                volgende_station = kies_opties_random(opties_huidig_station)
            if algo == 'G':
                volgende_station = kies_opties_greedy(opties_huidig_station, huidig_station.naam, self.netwerk.gereden_verbindingen)
            verbinding = self.verbindingen_lijst.zoek_verbinding(huidig_station.naam, volgende_station.naam)

            # Checkt of de tijdslimiet wordt overstreden
            if totale_tijd + verbinding.tijd > self.tijdslimiet:
                traject.traject_tijd = totale_tijd
                break
            traject.voeg_verbinding_toe(verbinding, self.netwerk.gereden_verbindingen) # Voegt de verbinding toe aan traject
            totale_tijd += verbinding.tijd # Update totale_tijd
            huidig_station = volgende_station


    # Controleert welke verbindingen nog niet zijn bezocht
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

        # Bepaal de niet bezochte verbindingen
        niet_bezochte_verbindingen = alle_verbindingen - bezochte_verbindingen

        return niet_bezochte_verbindingen

# Klasse om score van netwerk te berekenen
class Score:
    def __init__(self, netwerk, verbindingen_lijst):
        self.netwerk = netwerk
        self.verbindingen_lijst = verbindingen_lijst
        
    def bereken_score(self):
        aantal_bereden_verbindingen = len(self.netwerk.gereden_verbindingen)
        aantal_trajecten = len(self.netwerk.netwerk)
        totaal_verbindingen = len(self.verbindingen_lijst.verbindingen)
        Min = sum(traject.traject_tijd for traject in self.netwerk.netwerk)# Totale tijd

        score = (aantal_bereden_verbindingen / totaal_verbindingen ) * 10000 - (aantal_trajecten * 100 + Min)

        return score
