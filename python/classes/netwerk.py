class Netwerk:
    def __init__(self):
        # for aantal voeg traject toe en maak nieuw traject
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

    def alle_verbindingen_bereikt(self, verbindingen):
        return len(verbindingen.bezochte_verbindingen) == len(verbindingen.verbindingen)