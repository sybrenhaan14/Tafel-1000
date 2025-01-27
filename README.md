# RAIL NL Tafel-1000


## Projectopbouw

- **Code**: Hieraan staan de VSCODE-bestanden met alle codes. Deze map bevat een map met alle classes die we hebben gebruikt en hier bevindt zich ook een bestand met de code van de visualisatie.
- **Classes**: In deze map staan alle bestanden met de codes voor de verschillende classes die zijn gebruikt. We hebben gebruik gemaakt van zeven classes: stations, verbindingen, traject, netwerken, random_algo, Greedy en main. 
- **Data**: In deze map bevindt zich de map output en de CSV-bestanden met de data die we gebruiken.
- **Output**: In de map output bevindt zich de output van het random alogortime en de output van de tests
- **Docs**: Tot slot bevindt zich in deze map de datastructuur van het project.
- **Experiment**: 
- Onderaan bevindt zich de README, deze spreekt voor zich.

## 1. Projectbeschrijving

Het doel van dit project is om met behulp van algoritmes een lijnvoering te creëren met zeven trajecten in een tijdsframe van twee uur, waarin alle verbindingen worden berede en de score zo hoog mogelijk is. 
Voordat we dit voor heel Nederland hebben gedaan, hebben we op basis van een datatset van alle verbindingen in Noord- en Zuid Holland, code en algortimes geschreven een zo effectief mogelijke lijnvoering te creëren voor Holland. Toen we dit als basis hadden is de lijnvoering daarna uitgebreid naar heel Nederland en is er CSV-bestand gebruikt met alle verbindingen in Nederland. 

## 2 Code

### Classes:
- **Stations:** In de class stations wordt het CSV-bestand met de stations geladen en wordt er per station een lijst met opties samengesteld. 
- **Verbindingen:** In de class verbindingen wordt een lijst gemaakt van alle verbindingen en een set voor alle gereden verbindingen. 
- **Traject:** In deze class wordt gecheckt of een verbinding al is gereden en zo niet wordt de verbinding toegevoegd aan de lijst trajcet.
- **Lijnvoering:** In deze class worden de trajecten toegevoegd aan de lijst netwerk en wordt gecheckt of alle verbindingen worden gereden. Ook wordt de score berekent op basis van de gegeven formule. Het startstation wordt random gekozen uit de set stations, hier wordt dus gebruikt gemaakt van een random algortime.
- **Random_algo:** Voor elk station is eerder een lijst met opties samengesteld, uit deze opties wordt doormiddel van een random algoritme gekozen. De code hiervoor bevindt zich in deze class.
- **Greedy:** In deze class wordt gebruik gemaakt van het Greedy algoritme. In de lijst met opties wordt gecontroleerd of de verbinding al is gereden en als dit niet zo is wordt het station gekozen en wordt de verbinding toegevoegd aan de lijst met gereden verbindingen.

### Visualisatie

In de map code bevindt zich ook een file met de code van de visualisaties. We hebben verschillende visualisaties die ons project ondersteunen. Zo zijn er twee kaarten met alle verbindingen. De eerste kaart bevat een afbeelding van Holland met alle verbindingen en de tweede kaart is een kaart van heel Nederland met alle verbindingen die zich hierin bevinden. Tot slot hebben we een kaart gemaakt met de lijnvoering van het netwerk met de hoogste score, oftewel het beste netwerk. 

## 3 Verloop & argumentatie

Zoals eerder genoemd zijn we eerst aan de slag gegaan met de verbindingen in Holland. Voordat we gebruik zijn gaan maken van de algoritmes hebben we de verschillende classes ontworpen. Het eerste waar we tegen aanliepen was of we de code moesten schrijven vanuit het oogpunt stations of verbindingen. We hebben er toen voor gekozen om per station te kijken waar we heen konden en zo alle stations te rijden en niet twee keer over hetzelfde station te gaan. In eerste instantie lieten we het CSV-bestand elke keer inlezen om het volgende station te vinden. Aangezien dit steeds veel tijd in beslag nam, hebben we voor elk station een lijst met opties gemaakt. Vanaf nu wordt elke keeer deze lijst gelezen. Om te voorkomen dat een station vaker werd bereden, is er een lijst met bereden stations aangemaakt. We hebben uiteindelijk een code geschreven die over alle stations in Holland reed. Vervolgens kwamen we erachter dat het doel was om alle verbindingen te rijden en niet alle stations. De code is hierna omgeschreven zodat alle verbindingen werden gereden. Hierna is de code aangepast en is de lijnvoering gemaakt voor alle verbindingen in heel Nederland

### Random algoritme

Het eerste algoritme wat we hebben geïmplementeerd is het random algoritme. Dit algoritme maakt een keuze op basis van randomiteit. Het algortime is gebruikt bij het kiezen van een startstation en voor het kiezen van een volgend station. Dit is de eerste keer dat wij gebruik maken van een algoritme en het random algoritme is makkelijk te implementeren. Daarom is ervoor gekozen om dit algoritme in te zetten. (opvallende dingen na implementeren algoritme?)

### Greedy algoritme

Dit algoritme maakt de keus die op dat moment het voordeligst lijkt, zonder terug te kijken. Dit is het tweede algoritme wat we hebben geïmplementeerd. Het algoritme wordt gebruikt bij het kiezen van het volgende station en daarbij de keuze voor de volgende verbinding die wordt gereden. Het algoritme kiest voor de beste keus en dat is de kortst mogelijke verbinding die nog niet is gereden. Wanneer alle verbindingen al zijn gereden kiest het algoritme voor de kortste verbinding. Er is gekozen om de tijd van de verbinding een rol te laten spelen bij de keuze voor de beste optie. Er is hier voor gekozen aangezien we een tijdsframe van twee uur hebben om de lijnvoering uit te voeren, daarnaast draagt een kortere totale tijd bij aan een hogere score. (opvallende dingen na implementeren algoritme?)

### Experiment

## 4 Resultaten 

### Beperkingen
