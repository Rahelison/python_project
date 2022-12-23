from flight_map import FlightMap 

# Création de l'objet FlightMap
f = FlightMap()

# Chargement des aéroports depuis le fichier airports.csv
f.import_airports('airports.csv')

# Chargement des vols depuis le fichier flights.csv
f.import_flights('flights.csv')

# Accès à la liste des aéroports
print(f.airport())

# Accès à la liste des vols
print(f.flights())


print(str(f.airport_find("SYD")))