from verbindingen import Verbindingen

class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []
        self.traject_tijd = 0
        self.bezochte_stations = []

    def voeg_verbinding_toe(self, verbinding, gebruikte_verbindingen):
            print(f"Voegt verbinding toe: {verbinding}, Tijd verbinding: {verbinding.tijd}")
            self.traject.append(verbinding)
            self.traject_tijd += verbinding.tijd
            print(f"Totale traject tijd na toevoeging: {self.traject_tijd}")
            gebruikte_verbindingen.add((verbinding.id))

