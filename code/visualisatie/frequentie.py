import os
import pandas as pd

# Directory en output CSV-bestand
input_directory = "../../Data/outputs/random_Nationaal"
output_csv = "../../Data/outputs/frequenties/frequentie_random"

# Functie om een lijst met stations veilig te parseren
def schoonmaken_station_lijst(station_str):
    station_str = station_str.strip("[]")
    return [station.strip() for station in station_str.split(",")]
    

# Functie om verbindingen symmetrisch te maken
def symetrische_verbinding(verbinding):
    return tuple(sorted(verbinding))

# Lees bestaande frequenties of maak een nieuwe
if os.path.exists(output_csv):
    frequentie_df = pd.read_csv(output_csv)
else:
    frequentie_df = pd.DataFrame(columns=["Station A", "Station B", "Frequentie"])

# Zet bestaande data om naar dict
frequentie_dict = {
    (row["Station A"], row["Station B"]): row["Frequentie"] for _, row in frequentie_df.iterrows()
}

# lees bestanden in de directory
for bestand in os.listdir(input_directory):
    if bestand.endswith(".csv"):
        bestand_pad = os.path.join(input_directory, bestand)
        data = pd.read_csv(bestand_pad)

        # Zorg dat de stationskoloms kloppen
        data['stations'] = data['stations'].apply(schoonmaken_station_lijst)

        # Tel verbindingen per bestand
        bestand_verbindingen = {}
        for stations in data['stations']:
            for i in range(len(stations) - 1):
                verbinding = symetrische_verbinding((stations[i], stations[i + 1]))
                if verbinding in bestand_verbindingen:
                    bestand_verbindingen[verbinding] += 1
                else:
                    bestand_verbindingen[verbinding] = 1

        # Voeg de verbindingen toe aan de totale frequentie
        for verbinding, aantal in bestand_verbindingen.items():
            if verbinding in frequentie_dict:
                frequentie_dict[verbinding] += aantal
            else:
                frequentie_dict[verbinding] = aantal

# Zet de frequenties weer in df
bijgewerkte_frequentie_df = pd.DataFrame(
    [(verbinding[0], verbinding[1], freq) for verbinding, freq in frequentie_dict.items()],
    columns=["Station A", "Station B", "Frequentie"]
)

# Sla op
bijgewerkte_frequentie_df.to_csv(output_csv, index=False)


