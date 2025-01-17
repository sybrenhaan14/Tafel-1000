from verbindingen import Verbindingen

class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []
        self.gebruikte_verbindingen = set()  # Houd bij welke verbindingen al zijn gebruikt
        self.totale_tijd = 0
        self.bezochte_stations = []

    def voeg_verbinding_toe(self, verbinding):
        # Controleer of de verbinding al eerder is gebruikt
        if (verbinding.station1, verbinding.station2) not in self.gebruikte_verbindingen and \
           (verbinding.station2, verbinding.station1) not in self.gebruikte_verbindingen:
            self.traject.append(verbinding)
            self.gebruikte_verbindingen.add((verbinding.station1, verbinding.station2))
            self.totale_tijd += verbinding.tijd

            # Voeg station1 toe als het nog niet is toegevoegd
            if verbinding.station1 not in self.bezochte_stations:
                self.bezochte_stations.append(verbinding.station1)
            
            # Voeg station2 toe als het nog niet is toegevoegd
            if verbinding.station2 not in self.bezochte_stations:
                self.bezochte_stations.append(verbinding.station2)
