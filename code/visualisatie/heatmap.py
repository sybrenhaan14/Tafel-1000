import folium
import pandas as pd
import json
from folium.plugins import HeatMap
from matplotlib import cm, colors

# GeoJSON bestand laden van de kaart
def laad_geojson(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Stations laden uit het csv bestand
def laad_stations(file_path):
    stations_df = pd.read_csv(file_path)
    stations = {}
    for _, row in stations_df.iterrows():
        stations[row['station']] = [row['y'], row['x']]
    return stations

# frequenties laden uit het CSV bestand
def laad_frequenties(file_path):
    frequenties_df = pd.read_csv(file_path)
    frequenties = []
    for _, row in frequenties_df.iterrows():
        frequenties.append((row['station1'], row['station2'], row['frequentie']))
    return frequenties

# Kaart maken met GeoJSON beginnen in midden kaart
def maak_map_met_heatmap(geojson_data, stations, frequenties):
    map_nl = folium.Map(location=[52.3784, 4.9009], zoom_start=7)
    folium.GeoJson(geojson_data).add_to(map_nl)

    # Voeg heatmap-lijnen toe
    for station1, station2, frequentie in frequenties:
        if station1 in stations and station2 in stations:
            coord1 = stations[station1]
            coord2 = stations[station2]
            kleur = get_heatmap_kleur(frequentie)
            folium.PolyLine([coord1, coord2], color=kleur, weight=4, opacity=1).add_to(map_nl)

    return map_nl

# functie om kleuren te genereren voor lijnen op basis van frequentie
def get_heatmap_kleur(frequentie):
    
    norm = colors.LogNorm(vmin=10000, vmax=30000)  #lognorm om kleuren verder uit elkaar te laten staan in de verdeling
    cmap = cm._colormaps['plasma_r'] #nieuwe versie want de oude gaat binnenkort weg


    # frequentie naar RGBA en vervolgens naar hex zodat polyline hem kan gebruiken
    kleur = cmap(norm(frequentie))
    return colors.to_hex(kleur)

# laad GeoJSON
geojson_data = laad_geojson('../../Data/nl_regions.geojson')

# laad stations
stations_data = laad_stations('../../Data/StationsNationaal.csv')

# laad frequenties
frequenties_data = laad_frequenties('../../Data/outputs/frequenties_random_nationaal.csv')

# maak de kaart met heatmap-lijnen
map_nl_met_heatmap = maak_map_met_heatmap(geojson_data, stations_data, frequenties_data)

# Sla de kaart op
map_nl_met_heatmap.save('../../Docs/kaart_met_heatmap.html')

