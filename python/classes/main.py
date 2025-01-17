import random
from stations import *
from verbindingen import *
from netwerken import *
from verbinding import *
from netwerk import *
from traject import *
from score import *

def main():
    set_stations = Stations('../../Data/StationsHolland.csv')
    verbindingen_lijst = Verbindingen()

    netwerken = Netwerken(set_stations, verbindingen_lijst)
    netwerk = netwerken.genereer_trajecten()

    # Header voor de output
    print("train,stations")

    for traject in netwerk.netwerk:
        print(f'train_{traject.traject_id},"[{", ".join(traject.bezochte_stations)}]"')

    score_calculator = Score(netwerk)
    score = score_calculator.bereken_score()
    print(f'Score: {score}')

if __name__ == "__main__":
    main()
    # with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    #     writer = csv.writer(file)

    #     count = 0
    #     while count < 10000:
    #         data = main()  
    #         writer.writerows(data)
    #         count += 1
