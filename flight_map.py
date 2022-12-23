from typing import List
import csv
from airport import Airport
from flight import Flight
from flight_Path_broken import FlightPathBroken
from flight_path_duplicate import FlightPathDuplicate



class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
    
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file,'r') as f:
            reader = csv.reader(f,  delimiter=' ', quotechar='"')
            next(reader)

            for row in reader:
                name, code, lat, long = row
                lat, long = float(lat.replace(","," ")), float(long)
                code=code.replace(",","")
                airport = Airport(name, code, lat, long)
                self.airports.append(airport)
    
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, delimiter=' ', quotechar='"')
            next(reader)  
            for row in reader:
                src_code, dst_code, duration = row
                src_code,dst_code=src_code.replace(",",""),dst_code.replace(",","")
                duration = float(duration)
                flight = Flight(src_code, dst_code, duration)
                self.flights.append(flight)

    #  liste des aéroports
    def airports(self):
        return self.airports
    
    # list des flights
    def flights(self):
        return self.flights
    
    # Recherches simple d'aéroport par code
    def airport_find(self, airport_code: str) -> Airport:
        for airport in self.airports:
            if airport.code == airport_code:
                return airport
        return None
    
    # Vol direct entre deux aéroports
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for flight in self.flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
        return False
    
    #  Recherche des vols et aéroports accessibles à partir d'une ville donné
    def flights_where(self, airport_code: str) -> list[Flight]:
        return [flight for flight in self.flights if flight.src_code == airport_code or flight.dst_code == airport_code]
    
    def airports_from(self, airport_code: str) -> list[Airport]:
        flights = self.flights_where(airport_code)
        airport_codes = {flight.dst_code for flight in flights}
        return [self.airport_find(code) for code in airport_codes]


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:
        self.path = [src_airport]
        self.flights = []

# Initialise votre chemin avec l'aéroport de départ.
    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if dst_airport not in self.path[-1].destinations:
            raise FlightPathBroken("L'aéroport {} n'est pas la destination du dernier aéroport {} sur le chemin".format(dst_airport, self.path[-1]))
        if dst_airport in self.path:
            raise FlightPathDuplicate("L'aéroport {} est déjà sur le chemin".format(dst_airport))
        self.path.append(dst_airport)
        self.flights.append(via_flight)

    def flights(self) -> List[Flight]:
        return self.flights

    def airports(self) -> List[Airport]:
        return self.path

    def steps(self) -> float:
        return len(self.flights)

    def duration(self) -> float:
        return sum(flight.duration for flight in self.flights)

class FlightMap:
    def __init__(self, flights: List[Flight]) -> None:
        self.flights = flights
        self.airports = {flight.src for flight in flights} | {flight.dst for flight in flights}

    def paths(self, src_airport_code: str, dst_airport_code: str) -> List[FlightPath]:
        src_airport = self._get_airport(src_airport_code)
        dst_airport = self._get_airport(dst_airport_code)
        if src_airport is None or dst_airport is None:
            return []

        paths = []
        airports_not_visited = {airport for airport in self.airports}
        airports_future = {src_airport}
        airports_visited = set()
        while airports_future:
            airport = airports_future.pop()
            airports_not_visited.remove(airport)
            airports_visited.add(airport)
            if airport == dst_airport:
                paths.append(self._construct_path(src_airport, airport, airports_visited))
            else:
                for flight in self._get_outgoing_flights(airport):
                    if flight.dst in airports_not_visited:
                        airports_future.add(flight.dst)
        return paths

    def paths_shortest_length(self, src_airport_code: str, dst_airport_code: str) -> List[FlightPath]:
        paths = self.paths(src_airport_code, dst_airport_code)
        return [path for path in paths if path.steps() == min(path.steps() for path in paths)]

    def paths_shortest_duration(self, src_airport_code: str, dst_airport_code: str) ->List[FlightPath]:
        paths = self.path(src_airport_code, dst_airport_code)
        return[ path for path in paths if path.steps() == min(path.steps() for path in paths)]

