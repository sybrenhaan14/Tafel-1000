class Verbinding:
    def __init__(self, station1, station2, tijd):
        self.station1 = station1
        self.station2 = station2
        self.tijd = int(tijd)

    def __repr__(self):
        return f"{self.station1} -> {self.station2} ({self.tijd} min)"