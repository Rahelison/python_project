import csv
from airport import Airport
from flight import Flight
from flight_path import FlightPath


class FlightMap:
    def __init__(self):
        self.airports = {}
        self.flights = {}
    
    def import_airports(self, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # On crée un objet Airport avec les données lues
                airport = Airport(row[0], row[1], row[2], row[3])
                # On ajoute l'aéroport à la collection d'aéroports
                self.airports[row[0]] = airport
    
    def import_flights(self, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # On créé un objet Flight avec les données lues
                flight = Flight(row[0], row[1], float(row[2]))
                # On ajoute le vol à la collection de vols
                self.flights[(row[0])] = flight

    def airports(self):
        return list(self.airports.values())

    def flights(self):
        return list(self.flights.values())

    def airport_find(self, airport_code):
        try:
            return self.airports[airport_code]
        except KeyError:
                return None   

    def flight_exist(self, src_airport_code, dst_airport_code):
        return (src_airport_code, dst_airport_code) in self.flights
        

    def flights_where(self, airport_code):
        flights_list = []
        for flight in self.flights.values():
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights_list.append(flight)
            return flights_list

    def airports_from(self, airport_code):
        airports_list = []
        for flight in self.flights_where(airport_code):
            if flight.src_code == airport_code:
                airports_list.append(self.airport_find(flight.dst_code))
        else:
            airports_list.append(self.airport_find(flight.src_code))
            return airports_list  
            

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


