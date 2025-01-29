from code.classes.stations import Station, Stations
from code.classes.verbindingen import Verbindingen, Verbinding
from code.classes.netwerken import Netwerk, Lijnvoering
from code.classes.traject import Traject
from code.classes.algoritmes import Random, Greedy
import os 
import csv

class Main:
    def __init__(self):
        # Start de simulatie direct bij init
        self.stations_lijst = None
        self.verbindingen_lijst = None
        self.simulatie()

    def keuze_nl_of_holland(self):
        # Laat de gebruiker kiezen tussen Nederland of Holland
        while True:
            keuze = input("Kies Nationaal (N) of Holland (H): ").upper()
            if keuze == "N":
                return keuze
            elif keuze == "H":
                return keuze
            else:
                print("Ongeldige keuze. Kies N voor Nationaal of H voor Holland.")
    
    def keuze_random_of_greedy(self):
        # Laat de gebruiker kiezen tussen Random of Greedy algoritme
        while True:
            keuze = input("Kies Random (R) of Greedy (G): ").upper()
            if keuze == "R":
                return keuze
            elif keuze == "G":
                return keuze
            else:
                print("Ongeldige keuze. Kies R voor Random of G voor Greedy.")

     # Het netwerk wordt opgebouwd en de resultaten worden gegenereerd
    def main(self, regio, algo):
        station_lijst = self.stations_lijst
        verbindingen_lijst = self.verbindingen_lijst

        # Creëer een netwerk met trajecten
        lijnvoering = Lijnvoering(station_lijst, verbindingen_lijst, regio)
        netwerk = lijnvoering.genereer_trajecten(algo)

        # Voorbereiden van gegevens voor CSV-output
        output_data = []
        output_data.append(["train", "stations"])

        # Genereer output per traject
        for traject in netwerk.netwerk:
            output_data.append([f'train_{traject.traject_id}', f'[{", ".join(traject.bezochte_stations)}]'])

        # Bereken de score van het netwerk en voeg deze toe aan de output
        score = lijnvoering.bereken_score(netwerk, verbindingen_lijst)
        output_data.append([f'score', score])
        
        return output_data, score 

    # Simulatie meerdere keren uit te voeren en resultaten opslaan
    def simulatie(self):
        
        regio = self.keuze_nl_of_holland()
        keuze_algo = self.keuze_random_of_greedy()

        if regio == 'H':
            self.verbindingen_lijst = Verbindingen('Data/import_csv/ConnectiesHolland.csv')
            self.stations_lijst = Stations('Data/import_csv/StationsHolland.csv', self.verbindingen_lijst)
        elif regio == 'N':
            self.verbindingen_lijst = Verbindingen('Data/import_csv/ConnectiesNationaal.csv')
            self.stations_lijst = Stations('Data/import_csv/StationsNationaal.csv', self.verbindingen_lijst)
        
        # maakt de output directory
        if keuze_algo == 'R':
            algo = Random(self.stations_lijst, self.verbindingen_lijst)
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data', 'outputs', 'random_Holland')
        if keuze_algo == 'G':
            algo = Greedy(self.stations_lijst, self.verbindingen_lijst)
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data', 'outputs', 'greedy', 'break', 'Holland')
        count = 0
        

        # Voert de simulatie x aantal keer uit 
        for count in range(1, 100000):  
            print(count) # Houd bij bij welke itteratie we zijn 
            count =+ 1

            # Voert de simulatie uit en slaat resultaten op
            data, score = self.main(regio, algo)

            if data:
                
                # Maakt csv bestand aan 
                if regio == 'H':
                    output_bestand = os.path.join(output_dir, f"output_Holland_{score}.csv")
                if regio == 'N':
                    output_bestand = os.path.join(output_dir, f"output_Nationaal_{score}.csv")

                # Opent csv bestand en schrijft de uitkomst (netwerk) in het bestand.
                with open(output_bestand, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
            else:
                # Meld als er geen data wordt gegenereerd 
                print(f"Geen data om naar het bestand te schrijven voor simulatie {count}")
Main()