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

    for traject in netwerk.netwerk:
        print(f'Traject {traject.traject_id}:')
        for verbinding in traject.traject:
            print(f'  {verbinding}')
        print(f'Totaal tijd: {traject.bereken_totale_tijd()} minuten')


    niet_bezochte_verbindingen = netwerken.controleer_niet_bezochte_verbindingen()

    if niet_bezochte_verbindingen:
        print('Er zijn nog niet-bezochte stations:')
        for station in niet_bezochte_verbindingen:
            print(station)
    else:
        print('Alle stations zijn bezocht!')
        score_calculator = Score(netwerk)
        score = score_calculator.bereken_score()
        print(f'De kwaliteit van de lijnvoering (score) is: {score}')
        return True

if __name__ == "__main__":
    count = 0
    while (True):
        count =+ 1
        main()
        if main():
            break
    print(count)
