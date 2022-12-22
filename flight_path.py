from typing import List
from airport import Airport
from flight import Flight
from flight_path_broken import FlightPathBroken
import flight_map

class FlightPath:
    def __init__(self, src_airport: Airport):
        self.src_airport = src_airport
        self.flights = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if not self.flights or self.flights[-1].dst_code == via_flight.src_code:
            self.flights.append(via_flight)
        else:
            raise FlightPathBroken(f"Le vol {via_flight.src_code}-{via_flight.dst_code} ne passe pas par l'aéroport {self.flights[-1].dst_code}")

    def flights(self) -> List[Flight]:
        return self.flights

    def airports(self) -> List[Airport]:
        return [self.src_airport] + [flight_map.airport_find(flight.dst_code) for flight in self.flights]

    def steps(self) -> int:
        return len(self.flights)

    def duration(self) -> float:
        return sum(flight.duration for flight in self.flights)