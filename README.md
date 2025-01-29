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

### Gebruik
Een voorbeeld van het runnen van het is, dan krijg je een popup voor het welke regio je wil runnen en dan voor welk algoritme je wil runnen. Ook kunnen je in de code zelf aanpassen hoe vaak je het wil runnen.
`python main.py`

### Visualisatie

In de map code bevindt zich ook een file met de code van de visualisaties. We hebben verschillende visualisaties die ons project ondersteunen. Zo zijn er twee kaarten met alle verbindingen. De eerste kaart bevat een afbeelding van Holland met alle verbindingen en de tweede kaart is een kaart van heel Nederland met alle verbindingen die zich hierin bevinden. Tot slot hebben we een kaart gemaakt met de lijnvoering van het netwerk met de hoogste score, oftewel het beste netwerk.

## 3 Verloop & argumentatie

Zoals eerder genoemd zijn we eerst aan de slag gegaan met de verbindingen in Holland. Voordat we gebruik zijn gaan maken van de algoritmes hebben we de verschillende classes ontworpen. Het eerste waar we tegen aanliepen was of we de code moesten schrijven vanuit het oogpunt stations of verbindingen. We hebben er toen voor gekozen om per station te kijken waar we heen konden en zo alle stations te rijden en niet twee keer over hetzelfde station te gaan. In eerste instantie lieten we het CSV-bestand elke keer inlezen om het volgende station te vinden. Aangezien dit steeds veel tijd in beslag nam, hebben we voor elk station een lijst met opties gemaakt. Vanaf nu wordt elke keeer deze lijst gelezen. Om te voorkomen dat een station vaker werd bereden, is er een lijst met bereden stations aangemaakt. We hebben uiteindelijk een code geschreven die over alle stations in Holland reed. Vervolgens kwamen we erachter dat het doel was om alle verbindingen te rijden en niet alle stations. De code is hierna omgeschreven zodat alle verbindingen werden gereden. Hierna is de code aangepast en is de lijnvoering gemaakt voor alle verbindingen in heel Nederland

### Random algoritme

Het eerste algoritme wat we hebben geïmplementeerd is het random algoritme. Dit algoritme maakt een keuze op basis van randomiteit. Het algortime is gebruikt bij het kiezen van een startstation en voor het kiezen van een volgend station. Dit is de eerste keer dat wij gebruik maken van een algoritme en het random algoritme is makkelijk te implementeren. Daarom is ervoor gekozen om dit algoritme in te zetten. (opvallende dingen na implementeren algoritme?)

### Greedy algoritme

Dit algoritme maakt de keus die op dat moment het voordeligst lijkt, zonder terug te kijken. Dit is het tweede algoritme wat we hebben geïmplementeerd. Het algoritme wordt gebruikt bij het kiezen van het volgende station en daarbij de keuze voor de volgende verbinding die wordt gereden. Het algoritme kiest voor de beste keus en dat is de kortst mogelijke verbinding die nog niet is gereden. Wanneer alle verbindingen al zijn gereden kiest het algoritme voor de kortste verbinding. Er is gekozen om de tijd van de verbinding een rol te laten spelen bij de keuze voor de beste optie. Er is hier voor gekozen aangezien we een tijdsframe van twee uur hebben om de lijnvoering uit te voeren, daarnaast draagt een kortere totale tijd bij aan een hogere score. (opvallende dingen na implementeren algoritme?)

### Experimenteren met algoritmes

Een van de problemen waar wij tegen aan zijn gelopen had te maken met het Greedy algoritme. We laten het algoritme de beste keus maken, hierdoor kiest hij de kortste optie die niet is gereden. We laten het algoritme lopen tot 180 minuten lopen, maar met deze voorwaardes die we aan het algoritme hebben gehangen krijgen we niet een optimaal resultaat. Wanneer alle opties van bepaalde zijn gereden en  twee stations elkaars kortste opties zijn zullen ze steeds naar elkaar rijden. Hierdoor zullen er minder verbindingen worden gereden dan we willen en één bepaalde verbinding heel vaak. Hierdoor kregen we altijd een negatieve score. Met behulp van een experiment willen we erachter komen hoe we dit kunnen vermijden.

De huidige code kiest de verbinding die mogelijk is vanuit dat station met de kortste tijd. Dit hebben we proberen op te lossen op twee manieren. In eerste instantie hebben we de code zo herschreven dat wanneer alle mogelijke verbindingen al zijn gereden het algoritme een random keus maakt uit de mogelijke stations. Daarna hebben we de code aangepast dat het traject stopt wanneer alle opties al zijn gereden. Beide aanpassing hebben we 10.000 keer gerund en er zijn ook met deze aanpassingen geen positieve scores gevonden. 

Een volgens experiment wat we hebben uitgevoerd was met een maximaal aantal herhalingen. Er is een code geschreven waarbij opties die al gereden waren tot 3 keer toe konden worden gekozen. Er werd gebruikt gemaakt van een tel variabel, die elke kee hoger werd alas een het volgende station al in de lijst stond met gereden stations. Met deze aangepaste code hebben we het algoritme opnieuw 10.000 keer laten runnen, maar nog steeds bleken alle scores negatief. 

Daarnaast kiezen we nu met behulp van een random algoritme een start station, maar we waren benieuwd of er effectievere startstations zijn. In volgend experiment hebbenn we dit gestest. De aangepaste code voor dit experiment koos een startstation die maar 1 verbinding had. Na het runnen van de aangepaste code waren opnieuw alle scores negatief. 

## 4 Resultaten 

Uit onze output blijk dat er bij het gebruik van een random algoritme voornamelijk hoge positieve scores komen. Zowel op het niveau van Holland als op Nationaal niveau. Het Greedy algortime geeft daarentegen op niveau van Holland met name negatieve scores en op Nationaal niveua alleen maar negatieve scores. 

### Beperkingen

Opvallend aan onze resultaten is dat met het random algoritme er overwegened veel hoge positieve scores worden gevonden en met het Greedy algoritme op enkele na alleen maar negatieve scores vindt. Zelf bij het uitvoeren van meerdere experimenten op het Greedy algoritme, blijven de scores negatief. Dit is te verklaren uit de werking van de algoritmes. Het Greedy algoritme kiest altijd de beste optie, zonder terug of vooruit te kijken. Hierdoor houdt het algoritme geen rekeneing met de gevolgen die de keus kan hebben op het gehele netwerk. Hierdoor ontstaan situaties waarin het algoritme verbindingen niet efficiënt benut. Het gebruik van het Greedy algoritme kan leiden tot trajecten die niet efficiënt zijn en daardoor een negatieve score. Een ander mogelijke oorzaak voor de lage score zijn het aantal verbindingen dat er wordt gereden tijdens het gebruik van het Greedy algoritme. Zo worden er steeds maar 42 van de 89 verbindingen gereden, hierdoor valt de score ook lager uit. 

Het random algoritme houdt geen rekening met welke optie het best is. Ondanks dat dit algoritme geen rekening houdt met de beste opties, kiest het per toeval verbindingen die een netwerk creëren met een hogere score. 
