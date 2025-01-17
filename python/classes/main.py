import random
from stations import *
from verbindingen import *
from netwerken import *
from verbinding import *
from netwerk import *
from traject import *
from score import *
import os 

import csv

def main():
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




def simulatie():
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Data', 'outputs')

    
    for count in range(1, 100000):  
        
        data, score = main()

        if data:
            
            output_file = os.path.join(output_dir, f"holland_{score}.csv")

            
            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
        else:
            print(f"Geen data om naar het bestand te schrijven voor simulatie {count}")


simulatie()
