class Score:
    def __init__(self, netwerk):
        self.netwerk = netwerk

    def bereken_score(self):
        aantal_bereden_verbindingen = len(self.netwerk.netwerk)
        aantal_trajecten = len(self.netwerk.netwerk)
        Min = sum(verbinding.tijd for traject in self.netwerk.netwerk for verbinding in traject.traject)

        if aantal_bereden_verbindingen == 0:  # Om deling door 0 te voorkomen
            score = 0
        else:
            score = (aantal_bereden_verbindingen / 28 ) * 10000 - (aantal_trajecten * 100 + Min)

        return score

