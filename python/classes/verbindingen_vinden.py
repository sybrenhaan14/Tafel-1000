Class Vinden:


def verbindingen_vinden(huidig_station, opties, traject, station_set):
    totale_tijd = 0
    while totale_tijd < 120:
        # Gebruik opties om de eerste verbinding te kiezen
        station_set.is_bezocht(huidig_station)

        # Kies een volgende verbinding met voorkeur voor niet-bezochte stations
        volgende_station = opties.kies_opties(huidig_station, station_set.bezochte_stations)
        if not volgende_station:
            break  # Geen verdere verbindingen mogelijk

        # Zoek de verbinding tussen het huidige en volgende station
        verbinding = next(
            (v for v in opties.verbindingen.verbindingen
             if (v.station1 == huidig_station and v.station2 == volgende_station) or
                (v.station2 == huidig_station and v.station1 == volgende_station)),
            None
        )
        if not verbinding:
            break

        # Controleer of de tijdslimiet niet wordt overschreden
        if totale_tijd + verbinding.tijd > 120:
            break

        # Voeg de verbinding toe en werk de tijd en het huidige station bij
        traject.voeg_verbinding_toe(verbinding)
        totale_tijd += verbinding.tijd
        huidig_station = volgende_station

    return traject
