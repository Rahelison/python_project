class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float) -> None:
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration
    

    def __str__(self) -> str:
	    return f"source : {self.src_code}, dest : {self.dst_code}, duration: {self.duration}"    