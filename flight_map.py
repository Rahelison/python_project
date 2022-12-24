import csv
from airport import Airport
from flight import Flight
from flight_path import FlightPath

def formatCsvString(text: str) -> str:
    return text.replace('"', "").replace(" ", "")


class FlightMap:
    def __init__(self) -> None:
        self.airports = {}
        self.flights = {}
    
    def import_airports(self, csv_file: str) -> None:

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                name, code, latitude, longitude = row

                #formater les données récupérées
                name, code = formatCsvString(name), formatCsvString(code)
                latitude = float(formatCsvString(latitude))
                longitude = float(formatCsvString(longitude))

                airport = Airport(name, code, latitude, longitude)

                self.__airports[code] = airport
    
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                origin, destination, duration = row

                origin, destination = formatCsvString(origin), formatCsvString(destination)

                try :
                    duration = float(duration)
                except ValueError:
                    print('Something wrong on the CSV file')
                    continue

                flight = Flight(origin, destination, duration)
                self.__flights.append(flight)

    def airports(self) -> list[Airport]:
        return self.__airports.values()

    def flights(self) -> list[Flight]:
        return self.__flights

    def airport_find(self, airport_code: str) -> Airport:
        try:
            airport = self.__airports[airport_code]
            return airport
        except KeyError:
            print(f"The airport {airport_code} haven't been found !")
            return None  

    def flight_exist(self, src_airport_code, dst_airport_code: str) -> bool:
        for flight in self.__flights:
            if flight.src_code == src_airport_code \
                and flight.dst_code == dst_airport_code:
                return True
            else : 
                return False	
        

    def flights_where(self, airport_code: str) -> list[Flight]:
        flights = []
        for flight in self.__flights:
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights.append(flight)
                
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        destinations = []

        for flight in self.__flights:

            if flight.src_code == airport_code:
                airport = self.__airports[flight.dst_code]
            elif flight.dst_code == airport_code:
                    airport =  self.__airports[flight.src_code]
            else : 
                    continue

        if airport not in destinations:
            print(airport.code)
            destinations.append(airport)

            return destinations 
            

    def paths(self, src_airport_code, dst_airport_code):
        # Initialisation
        airports_not_visited = set(self.airports.keys())
        airports_future = set()
        airports_visited = set()
        FlightPaths = []

        # Ajout du point de départ à la liste des aéroports à visiter
        airports_future.add(src_airport_code)
        
        # Tant qu'il reste des villes à visiter
        while airports_future:
            # On prend l'aéroport à visiter
            airport = airports_future.pop()
            
            # On l'ajoute à la liste des aéroports visités
            airports_visited.add(airport)
            
            # On enlève l'aéroport de la liste des aéroports non visités
            airports_not_visited.remove(airport)
            
            # On récupère les vols partant de l'aéroport
            flights = self.flights_from(airport)
            
            for flight in flights:
                # On ajoute la destination de chaque vol à la liste des aéroports à visiter
                if flight.dst_airport_code not in airports_future:
                    airports_future.add(flight.dst_airport_code)
                    
                # On enlève la destination de chaque vol de la liste des aéroports non visités
                if flight.dst_airport_code in airports_not_visited:
                    airports_not_visited.remove(flight.dst_airport_code)
                    
                # On ajoute le vol à la liste des chemins possibles
                FlightPaths.append(FlightPath(flight))
                
            # Si on a trouvé la destination, on arrête la boucle
            if dst_airport_code in airports_future:
                break
        
        return FlightPaths

    def paths_shortest_length(self, src_airport_code, dst_airport_code):
        # Initialisation
        airports_not_visited = set(self.airports.keys())
        airports_future = set()
        airports_visited = set()
        FlightPaths = []
        shortest_paths = []

        # Ajout du point de départ à la liste des aéroports à visiter
        airports_future.add(src_airport_code)
        
        # Tant qu'il reste des villes à visiter
        while airports_future:
            # On prend l'aéroport à visiter
            airport = airports_future.pop()
            
            # On l'ajoute à la liste des aéroports visités
            airports_visited.add(airport)
            
            # On enlève l'aéroport de la liste des aéroports non visités
            airports_not_visited.remove(airport)
            
            # On récupère les vols partant de l'aéroport
            flights = self.flights_from(airport)
            
            for flight in flights:
                # On ajoute la destination de chaque vol à la liste des aéroports à visiter
                if flight.dst_airport_code not in airports_future:
                    airports_future.add(flight.dst_airport_code)
                    
                # On enlève la destination de chaque vol de la liste des aéroports non visités
                if flight.dst_airport_code in airports_not_visited:
                    airports_not_visited.remove(flight.dst_airport_code)
                    
                # On ajoute le vol à la liste des chemins possibles
                FlightPaths.append(FlightPath(flight))
                
            # Si on a trouvé la destination, on arrête la boucle
            if dst_airport_code in airports_future:
                # On calcule la longueur du chemin
                path_length = len(airports_visited)
                
                # On ajoute le chemin à la liste des chemins minimaux
                if shortest_paths == [] or len(shortest_paths[0]) == path_length:
                    shortest_paths.append(FlightPaths)
                elif len(shortest_paths[0]) > path_length:
                    shortest_paths = [FlightPaths]
                    
                # On réinitialise les variables
                FlightPaths = []
                airports_future = set()
                airports_visited = set()
        
        # On retourne la liste des chemins minimaux
        return shortest_paths


    def paths_shortest_duration(self, src_airport_code, dst_airport_code):
        # Initialisation
        airports_not_visited = set(self.airports.keys())
        airports_future = set()
        airports_visited = set()
        FlightPaths = []
        shortest_paths = []

        # Ajout du point de départ à la liste des aéroports à visiter
        airports_future.add(src_airport_code)
        
        # Tant qu'il reste des villes à visiter
        while airports_future:
            # On prend l'aéroport à visiter
            airport = airports_future.pop()
            
            # On l'ajoute à la liste des aéroports visités
            airports_visited.add(airport)
            
            # On enlève l'aéroport de la liste des aéroports non visités
            airports_not_visited.remove(airport)
            
            # On récupère les vols partant de l'aéroport
            flights = self.flights_from(airport)
            
            for flight in flights:
                # On ajoute la destination de chaque vol à la liste des aéroports à visiter
                if flight.dst_airport_code not in airports_future:
                    airports_future.add(flight.dst_airport_code)
                    
                # On enlève la destination de chaque vol de la liste des aéroports non visités
                if flight.dst_airport_code in airports_not_visited:
                    airports_not_visited.remove(flight.dst_airport_code)
                    
                # On ajoute le vol à la liste des chemins possibles
                FlightPaths.append(FlightPath(flight))
                
            # Si on a trouvé la destination, on arrête la boucle
            if dst_airport_code in airports_future:
                # On calcule la durée du chemin
                path_duration = sum([f.duration for f in FlightPaths])
                
                # On ajoute le chemin à la liste des chemins minimaux
                if shortest_paths == [] or shortest_paths[0].duration == path_duration:
                    shortest_paths.append(FlightPaths)
                elif shortest_paths[0].duration > path_duration:
                    shortest_paths = [FlightPaths]
                    
                # On réinitialise les variables
                FlightPaths = []
                airports_future = set()
                airports_visited = set()
        
        # On retourne la liste des chemins minimaux
        return shortest_paths


    def paths_via(self, src_airport_code, dst_airport_code, via_airport_code):
        # Initialisation
        FlightPaths = []
        via_paths = []
        
        # On vérifie que le vol direct existe
        if self.flight_exist(src_airport_code, via_airport_code):
            # On récupère les chemins possibles depuis le point de départ jusqu'à l'escale
            src_via_paths = self.paths(src_airport_code, via_airport_code)
            
            # On récupère les chemins possibles depuis l'escale jusqu'à la destination
            via_dst_paths = self.paths(via_airport_code, dst_airport_code)
            
            # Pour chaque chemin depuis le point de départ jusqu'à l'escale
            for src_via_path in src_via_paths:
                # On récupère les vols qui composent le chemin
                src_via_flights = src_via_path.flights
                
                # Pour chaque chemin depuis l'escale jusqu'à la destination
                for via_dst_path in via_dst_paths:
                    # On récupère les vols qui composent le chemin
                    via_dst_flights = via_dst_path.flights
                    
                    # On crée un nouveau chemin à partir des vols des deux chemins
                    new_path = FlightPath(*src_via_flights + via_dst_flights)
                    
                    # On ajoute le nouveau chemin à la liste des chemins possibles
                    via_paths.append(new_path)
            
        # On retourne la liste des chemins
        return via_paths


