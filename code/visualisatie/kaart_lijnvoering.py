import pandas as pd
import folium  
from folium import Map, PolyLine, CircleMarker
from collections import defaultdict
from itertools import cycle
import random

# Laad de data
trein_data = pd.read_csv("../../Data/outputs/random_Nationaal/output_Nationaal_3983.8426966292136.csv")
stations_data = pd.read_csv("../../Data/import_csv/StationsNationaal.csv")

# Maak een dictionary voor coördinaten
stations_dict = {}
for index, row in stations_data.iterrows():
    station_naam = row['station']
    stations_dict[station_naam] = {'y': row['y'], 'x': row['x']}

# Functie om random kleuren te genereren
def random_kleur():
    r = random.choice(range(256))
    g = random.choice(range(256))
    b = random.choice(range(256))
    return f"#{r:02x}{g:02x}{b:02x}"

# Functie om stationsnamen om te zetten naar coördinaten
def get_coordinaten(stations_lijst):
    coordinaten = []
    for station in stations_lijst:
        if station in stations_dict:
            coordinaat = [stations_dict[station]['y'], stations_dict[station]['x']]
            coordinaten.append(coordinaat)
    return coordinaten

# Functie om een gestreepte lijn met meerdere kleuren toe te voegen
def voeg_gestreepte_lijn_toe(segment, kleuren, kaart_object):
    kleur_cyclus = cycle(kleuren)  # Checkt kleuren van beide treinen
    dash_styles = ["10, 10", "5, 5"]  # Maakt verschillende patronen aan voor duidelijkheid

    for i, kleur in enumerate(kleuren):
        PolyLine(
            locations=list(segment),
            color=kleur,
            weight=4,
            dash_array=dash_styles[i % len(dash_styles)] # pakt of 10, 10 of 5, 5 als stijl
        ).add_to(kaart_object)

# Initialiseer midden op kaart nl
trein_kaart = Map(location=[52.3784, 4.9009], zoom_start=7)

# Dictionary om gedeelde trajecten en kleuren die daarbij horen bijhouden
gedeelde_routes = defaultdict(list)
trein_kleuren = {}

# Verwerk trein en houd gedeelde trajecten bij
for index, row in trein_data.iterrows():
    trein_naam = row['train']
    stations_raw = row['stations']
    stations_zonder_haken = stations_raw.strip("[]")
    stations_zonder_aanhalingstekens = stations_zonder_haken.replace("'", "")
    stations_lijst = stations_zonder_aanhalingstekens.split(", ")

    route_coordinaten = get_coordinaten(stations_lijst)
    kleur = random_kleur()
    trein_kleuren[trein_naam] = kleur

    for i in range(len(route_coordinaten) - 1):
        start_punt = tuple(route_coordinaten[i])
        eind_punt = tuple(route_coordinaten[i + 1])
        segment = tuple(sorted((start_punt, eind_punt)))

        # Controleer of het segment al bestaat in de gedeelde routes
        if segment not in gedeelde_routes:
            gedeelde_routes[segment] = []

        # Voeg de kleur toe aan de lijst van het segment
        gedeelde_routes[segment].append(kleur)

# Voeg trajecten toe aan de kaart
for segment, kleuren in gedeelde_routes.items():
    if len(kleuren) > 1:
        voeg_gestreepte_lijn_toe(segment, kleuren, trein_kaart)
    else:
        PolyLine(locations=list(segment), color=kleuren[0], weight=4).add_to(trein_kaart)

# Voeg stationspunten toe aan de kaart dmv circlemarker
for _, station_row in stations_data.iterrows():
    station_naam = station_row['station']
    station_lat = station_row['y']
    station_lon = station_row['x']
    CircleMarker(
        location=[station_lat, station_lon],
        radius=3,
        color="blue",
        fill=True,
        tooltip=station_naam,
        popup=station_naam
    ).add_to(trein_kaart)

# Sla de kaart op
trein_kaart.save("../../Docs/kaart_lijnvoering_nationaal.html")


