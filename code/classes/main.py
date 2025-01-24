import random
from stations import *
from verbindingen import *
from netwerken import *
from traject import *
import os 
import csv

class Main:
    def __init__(self):
        # Start de simulatie direct bij init
        
        self.simulatie()



    def keuze_nl_of_holland(self):
        """Laat de gebruiker kiezen tussen Nederland of Holland"""
        while True:
            keuze = input("Kies Nederland (N) of Holland (H): ").upper()
            if keuze == "N":
                return keuze
            elif keuze == "H":
                return keuze
            else:
                print("Ongeldige keuze. Kies N voor Nederland of H voor Holland.")
    
    def keuze_random_of_greedy(self):
        """Laat de gebruiker kiezen tussen Random of Greedy algoritme"""
        while True:
            keuze = input("Kies Random (R) of Greedy (G): ").upper()
            if keuze == "R":
                return keuze
            elif keuze == "G":
                return keuze
            else:
                print("Ongeldige keuze. Kies R voor Random of G voor Greedy.")

     # Het netwerk wordt opgebouwd en de resultaten worden gegenereerd
    def main(self):

        # Initialiseer stations en verbindingen
        regio = self.keuze_nl_of_holland()
        if regio == 'H':
            verbindingen_lijst = Verbindingen('../../Data/ConnectiesHolland.csv')
            station_lijst = Stations('../../Data/StationsHolland.csv', verbindingen_lijst)

        if regio == 'N':
            verbindingen_lijst = Verbindingen('../../Data/ConnectiesNationaal.csv')
            station_lijst = Stations('../../Data/StationsNationaal.csv', verbindingen_lijst)

        algo = self.keuze_random_of_greedy()
        # Creëer een netwerk met trajecten
        netwerken = Netwerken(station_lijst, verbindingen_lijst)
        netwerk = netwerken.genereer_trajecten(algo)

        # Voorbereiden van gegevens voor CSV-output
        output_data = []
        output_data.append(["train", "stations"])

        # Genereer output per traject
        for traject in netwerk.netwerk:
            output_data.append([f'train_{traject.traject_id}', f'[{", ".join(traject.bezochte_stations)}]'])

        # Bereken de score van het netwerk en voeg deze toe aan de output
        score_uitrekenen = Score(netwerk)
        score = score_uitrekenen.bereken_score()
        output_data.append([f'score', score])

        # print("Output Data:", output_data)
        # print("Score:", score)
        
        return output_data, score 

    # Simulatie meerdere keren uit te voeren en resultaten opslaan
    def simulatie(self):
        
        # maakt de output directory
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Data', 'outputs', 'test')
        count = 0
        
        # Voert de simulatie x aantal keer uit 
        for count in range(1, 10):  
            print(count) # Houd bij bij welke itteratie we zijn 
            count =+ 1

            # Voert de simulatie uit en slaat resultaten op
            data, score = self.main()

            if data:
                
                # Maakt csv bestand aan 
                output_bestand = os.path.join(output_dir, f"holland_{score}.csv")

                # Opent csv bestand en schrijft de uitkomst (netwerk) in het bestand.
                with open(output_bestand, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
            else:
                # Meld als er geen data wordt gegenereerd 
                print(f"Geen data om naar het bestand te schrijven voor simulatie {count}")
Main()