class Airport:
    def __init__(self, name: str = "", code: str = "", lat: float = 0, long: float = 0) -> None:
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

    def __str__(self) -> str:
	    print(f"Aéroport {self.name} : \n Code = {self.code} \n")    