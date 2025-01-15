class Netwerk:
    def __init__(self):
        # for aantal voeg traject toe en maak nieuw traject
        self.netwerk = []

    def voeg_traject_toe(self, traject):
        self.netwerk.append(traject)

    def alle_stations_bereikt(self, set_stations):
        #Controleer of alle stations zijn aangetikt
        bezochte_stations = set()
        for traject in self.netwerk:
            for verbinding in traject.traject:
                bezochte_stations.add(verbinding.station1)
                bezochte_stations.add(verbinding.station2)

        return bezochte_stations == set_stations