from dataclasses import dataclass
@dataclass
class ticket():
    movie : str = ""
    date : str = ""
    time : str = ""
    name : str = ""
    seat : str = ""
    price : float = 0.0 

customers = [ticket() for i in range(5)]

customers[0].movie = "Spiderman"
customers[0].date = "29/07/2026"
customers[0].time = "19:00"
customers[0].name = "Zeus Halloway"
customers[0].seat = "H9"
customers[0].float = 10.99
