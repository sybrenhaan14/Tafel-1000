class Score:
    def __init__(self, netwerk):
        self.netwerk = netwerk
        self.T = 0  
        self.Min = 0  
        self.p = 1  
        self.score = 1  

    def bereken_score(self):
        
        self.Min = sum(verbinding.tijd for traject in self.netwerk.netwerk for verbinding in traject.traject)

        self.T = sum(1 for traject in self.netwerk.netwerk if traject.bereken_totale_tijd() > 0)

        
        self.score = 10000 - (self.T * 100 + self.Min)

        return self.score

