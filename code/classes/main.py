import random
from stations import *
from verbindingen import *
from netwerken import *
from traject import *
import os 

import csv
class Main:
    def __init__(self):
        self.simulatie()


    def main(self):
        set_stations = Stations('../../Data/StationsHolland.csv')
        verbindingen_lijst = Verbindingen()

        netwerken = Netwerken(set_stations, verbindingen_lijst)
        netwerk = netwerken.genereer_trajecten()

        
        output_data = []

        
        output_data.append(["train", "stations"])

        # Genereer output per traject
        for traject in netwerk.netwerk:
            output_data.append([f'train_{traject.traject_id}', f'[{", ".join(traject.bezochte_stations)}]'])

        score_calculator = Score(netwerk)
        score = score_calculator.bereken_score()
        output_data.append([f'score', score])

        
        return output_data, score 

    def simulatie(self):
        
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Data', 'extra_outputs')
        count = 0
        
        for count in range(1, 10):  
            print(count)
            count =+ 1
            data, score = self.main()

            if data:
                
                output_file = os.path.join(output_dir, f"holland_{score}.csv")

                
                with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
            else:
                print(f"Geen data om naar het bestand te schrijven voor simulatie {count}")


Main()