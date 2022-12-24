from airport import Airport
from flight_map import FlightMap
# a = Airport("Paris Charles de Gaulle", "CDG", 49.012779, 2.55)

# print(a.name, a.code, a.lat, a.long) 

class Test:

    def setup_method(self):
        self.flight_map = FlightMap()

    def test_import_airports(self):
        self.flight_map.import_airports('airports.csv')
        assert len(self.flight_map.airports) == 3

    def test_import_flights(self):
        self.flight_map.import_flights('flights.csv')
        assert len(self.flight_map.flights) == 3

    