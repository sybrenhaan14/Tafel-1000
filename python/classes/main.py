import random
from stations import *
from verbindingen import *
from netwerken import *
from verbinding import *
from netwerk import *
from traject import *

set_stations = Stations('../Data/StationsHolland.csv')
verbindingen_lijst = Verbindingen()

netwerken = Netwerken(set_stations, verbindingen_lijst)
netwerk = netwerken.genereer_trajecten()

for traject in netwerk.netwerk:
    print(f"Traject {traject.traject_id}:")
    for verbinding in traject.traject:
        print(f"  {verbinding}")
    print(f"Totaal tijd: {traject.bereken_totale_tijd()} minuten\n")


niet_bezochte_stations = netwerken.controleer_niet_bezochte_stations()

if niet_bezochte_stations:
    print("Er zijn nog niet-bezochte stations:")
    for station in niet_bezochte_stations:
        print(station)
else:
    print("Alle stations zijn bezocht!")