from flight_map import FlightMap 

f= FlightMap()
f.import_airports('airports.csv')

print(f.airports())
