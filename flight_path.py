from flight import Flight
from flight_path_broken import FlightPathBroken
from flight_path_duplicate import FlightPathDuplicate
from airport import Airport

class FlightPath:
    def __init__(self, src_airport: Airport) -> None:
        self.airports = [src_airport]
        self.flights = []

    def add(self, dst_airport: Airport, via_flight : Flight) -> None:
        if not self.airports[-1] == via_flight.src_code:
            raise FlightPathBroken
        if self.airports.count(dst_airport) > 0:
            raise FlightPathDuplicate
        self.airports.append(dst_airport)
        self.flights.append(via_flight)

    def flights(self):
        return self.flights

    def airports(self):
        return self.airports

    def steps(self):
        return len(self.flights)

    def duration(self):
        return sum([f.duration for f in self.flights])



    
        