from flight_path_broken import FlightPathBroken
from flight_path_duplicate import FlightPathDuplicate

class FlightPath:
    def __init__(self, src_airport):
        self.airports = [src_airport]
        self.flights = []

    def add(self, dst_airport, via_flight):
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



    
        