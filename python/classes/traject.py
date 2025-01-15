class Traject:
    def __init__(self, traject_id):
        self.traject_id = traject_id
        self.traject = []

    def voeg_verbinding_toe(self, verbinding):
        self.traject.append(verbinding)

    def bereken_totale_tijd(self):
        return sum(verbinding.tijd for verbinding in self.traject)