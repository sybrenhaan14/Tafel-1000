from .verbindingen import Verbindingen

class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id # id per traject
        self.traject = [] # lijst voor alle verbindingen die zijn gereden
        self.traject_tijd = 0 # tijd voor het traject
        self.bezochte_stations = [] # lijst met alle bezochte stations

    def voeg_verbinding_toe(self, verbinding, gebruikte_verbindingen):
        # voeg de verbinding toe
        self.traject.append(verbinding)
        # update de tijd
        self.traject_tijd += verbinding.tijd
        # voeg de id van de verbinding toe aan gebruikte verbindingen
        gebruikte_verbindingen.add((verbinding.id))

