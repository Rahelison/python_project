#with open('airports.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)
    
#with open('flights.csv', 'r') as m:
#    reader = csv.reader(m)
#    for row in reader:
#        print(row)    

import csv
from airport import Airport
from flight import Flight 

class FlightMap:
    def __init__(self):
        self.airports = {} # dictionnaire des aéroports, indexé par leur code
        self.flights = [] # liste des vols

    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            next(reader) # on saute la première ligne (en-têtes)
            for row in reader:
                airport = Airport(row[0], row[1], float(row[2]), float(row[3]))
                self.airports[row[1]] = airport

    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            next(reader) # on saute la première ligne (en-têtes)
            for row in reader:
                flight = Flight(row[0], row[1], float(row[2]))
                self.flights.append(flight)