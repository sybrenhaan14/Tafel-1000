from verbindingen import *
class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []
        self.gebruikte_verbindingen = set()  # Houd bij welke verbindingen al zijn gebruikt
        self.totale_tijd = 0

    def voeg_verbinding_toe(self, verbinding):
        #Voeg een verbinding toe en update de totale tijd
        if (verbinding.station1, verbinding.station2) not in self.gebruikte_verbindingen and \
           (verbinding.station2, verbinding.station1) not in self.gebruikte_verbindingen:
            self.traject.append(verbinding)
            self.gebruikte_verbindingen.add((verbinding.station1, verbinding.station2))
            Verbindingen.is_bereden(verbinding)
            self.totale_tijd += verbinding.tijd

    def bereken_totale_tijd(self):
        # checkt totale tijd
        return self.totale_tijd
    
    def is_volledig(self, tijdslimiet=120):
        #Controleer of het traject de tijdslimiet overschrijdt
        return self.totale_tijd > tijdslimiet