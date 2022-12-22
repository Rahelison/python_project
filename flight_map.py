import csv
from typing import List
from unittest import result
from airport import Airport
from flight import Flight
from flight_path import FlightPath

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
    
    def import_airports(self, csv_file: str) -> None:
            
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                name, code, lat, long = row
                lat, long = float(lat), float(long)
                airport = Airport(name, code, lat, long)
                self.airports.append(airport)

                
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                src_code, dst_code, duration = row
                duration = float(duration)
                flight = Flight(src_code, dst_code, duration)
                self.flights.append(flight)


# Liste des aéroports

    def airports(self) -> List[Airport]:
        return list(self.airports.values())  

    def flights(self) -> List[Flight]:
        return list(self.flights.values())              
    
# Recherche d'aéroport

    def airport_find(self, airport_code: str) -> Airport:
        return self.airports.get(airport_code)

# Recherche de vol direct

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        return (src_airport_code, dst_airport_code) in self.flights

# Recherche de vols et aéroport accessibles à partir d'un aéroport donné

    def flights_where(self, airport_code: str) -> List[Flight]:
        return [flight for flight in self.flights.values()
        if flight.src_code == airport_code or flight.dst_code == airport_code]

    def airports_from(self, airport_code: str) -> List[Airport]:
        flights = self.flights_where(airport_code)
        return [self.airport_find(flight.dst_code)
        for flight in flights]       

    

    def paths(self, src_airport_code: str, dst_airport_code: str) -> List[FlightPath]:

        airports_not_visited = set(self.airports) # convertir la liste en ensemble pour une recherche plus rapide
        airports_future = []
        airports_visited = []

        # ajoutez l'aéroport de départ à la liste des aéroports à visiter
        airports_future.append(src_airport_code)
        
        distance = 0
        
        while airports_not_visited:
            
            distance += 1
            
            current_distance_airports = []
            
            for airport_code in airports_future:
                
                airports_not_visited.remove(airport_code)
                airports_visited.append(airport_code)
                flights_from_airport = self.get_flights_from_airport(airport_code)
                
                for flight in flights_from_airport:
                    
                    if flight.dst_airport_code == dst_airport_code:
                        result.append(FlightPath(src_airport_code, dst_airport_code, distance))
                        continue
                    
                    if flight.dst_airport_code not in airports_visited:
                        current_distance_airports.append(flight.dst_airport_code)
            
            airports_future = current_distance_airports
        
        return result

        def paths_shortest_length(self, src_airport_code: str, dst_airport_code: str) -> List[FlightPath]:
        
                airports_not_visited = set(self.airports) # convertir la liste en ensemble pour une recherche plus rapide
                airports_future = []
                airports_visited = []

        
        airports_future.append(src_airport_code)
        distance = 0
        result = []
        
        while airports_not_visited:
            
            distance += 1
            current_distance_airports = []
            
            for airport_code in airports_future:
                
                airports_not_visited.remove(airport_code)
                airports_visited.append(airport_code)
                flights_from_airport = self.get_flights_from_airport(airport_code)
                
                for flight in flights_from_airport:

                    if flight.dst_airport_code == dst_airport_code:
                        result.append(FlightPath(src_airport_code, dst_airport_code, distance))

                        continue
                    if flight.dst_airport_code not in airports_visited:
                        current_distance_airports.append(flight.dst_airport_code)
            
            airports_future = current_distance_airports


        def paths_shortest_duration(self, src_airport_code: str, dst_airport_code: str) -> List[FlightPath]:
        
            airports_not_visited = set(self.airports) 
            airports_future = []
            airports_visited = []
            airports_future.append(src_airport_code)
            duration = 0
            result = []
        
            while airports_not_visited:
            
                current_duration_airports = []
            
                for airport_code in airports_future:
                
                    airports_not_visited.remove(airport_code)
                    airports_visited.append(airport_code)
                    flights_from_airport = self.get_flights_from_airport(airport_code)
                
                for flight in flights_from_airport:
                    
                    duration += flight.duration
                    
                    if flight.dst_airport_code == dst_airport_code:
                        result.append(FlightPath(src_airport_code, dst_airport_code, duration))
                        continue
                    
                    if flight.dst_airport_code not in airports_visited:
                        current_duration_airports.append(flight.dst_airport_code)
            
                    airports_future = current_duration_airports