import folium
import pandas as pd
import json

# GeoJSON bestand laden
def laad_geojson(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# stations laden uit een CSV bestand
def laad_stations(file_path):
    stations_df = pd.read_csv(file_path)
    stations = {}
    for _, row in stations_df.iterrows():
        stations[row['station']] = [row['y'], row['x']]
    return stations

# treinverbindingen laden
def laad_verbindingen(file_path, stations):
    verbindingen = []
    verbindingen_df = pd.read_csv(file_path)
    for _, row in verbindingen_df.iterrows():
        station1 = row['station1']
        station2 = row['station2']
        
        # Controleer of de stations bestaan
        if station1 in stations and station2 in stations:
            verbindingen.append((stations[station1], stations[station2]))
    return verbindingen


def maak_map(geojson_data, verbindingen):
    # Start de kaart in midden nl
    map_nl = folium.Map(location=[52.3784, 4.9009], zoom_start=7)

    # Voeg de GeoJSON van Nederland toe
    folium.GeoJson(geojson_data).add_to(map_nl)

    # Voeg de treinverbindingen toe aan de kaart
    for verbinding in verbindingen:
        folium.PolyLine(verbinding, color="blue", weight=2.5, opacity=1).add_to(map_nl)

    return map_nl

# Laad GeoJSON 
geojson_data = laad_geojson('../Data/nl_regions.geojson')  # Geef het pad naar je GeoJSON bestand

# Laad de stations
stations = laad_stations('../Data/StationsNationaal.csv')

# Laad de treinverbindingen 
verbindingen = laad_verbindingen('../Data/ConnectiesNationaal.csv', stations)

# Maak de kaart
map_nl = maak_map(geojson_data, verbindingen)

# Sla de kaart op 
map_nl.save('kaart_verbindingen_Nationaal.html')
