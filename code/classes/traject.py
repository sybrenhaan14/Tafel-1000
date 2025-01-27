from verbindingen import Verbindingen

class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []
        self.traject_tijd = 0
        self.bezochte_stations = []

    def voeg_verbinding_toe(self, verbinding, gebruikte_verbindingen):
        # Controleer of de verbinding al eerder is gebruikt
        if (verbinding.station1, verbinding.station2) not in gebruikte_verbindingen and \
           (verbinding.station2, verbinding.station1) not in gebruikte_verbindingen:
            self.traject.append(verbinding)
            gebruikte_verbindingen.add((verbinding.id))

