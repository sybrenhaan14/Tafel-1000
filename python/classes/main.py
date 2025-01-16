import random
from stations import *
from verbindingen import *
from netwerken import *
from verbinding import *
from netwerk import *
from traject import *
from score import *

def main():
    set_stations = Stations('../Data/StationsHolland.csv')
    verbindingen_lijst = Verbindingen()

    netwerken = Netwerken(set_stations, verbindingen_lijst)
    netwerk = netwerken.genereer_trajecten()

    output = [("train", "stations")]
    for i, traject in enumerate(netwerk.netwerk, start=1):
        station_names = [verbinding.station1 for verbinding in traject.traject]
        if traject.traject:
            station_names.append(traject.traject[-1].station2)
        output.append((f"train_{i}", f"[{', '.join(station_names)}]"))

    
    score_calculator = Score(netwerk)
    score = score_calculator.bereken_score()
    output.append(("score", score))

    return output


if __name__ == "__main__":
    output_file = "output.csv"

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        count = 0
        while count < 10000:
            data = main()  
            writer.writerows(data)
            count += 1