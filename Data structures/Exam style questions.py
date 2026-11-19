from dataclasses import dataclass
@dataclass
class seat_details():
    customers_name : str = ""
    contact_phone_number : str = ""
    cost = float = 0.0
    sold = bool = False

seats = [[seat_details() for i in range(4)] for j in range(13)]

for i in range(len(seats)*len(seats[0])):
    row = i%len(seats)
    col = i//len(seats[0])

    if (i== 23 or i==24 or i==27 or i==28):
        seats[row][col].customers = "Toilet"
        seats[row][col].contact_phone_number = "Null"
        seats[row][col].cost = 0.0
        seats[row][col].sold = True
    else:
        seats[row][col].customers = "Empty"
        seats[row][col].contact_phone_number = "Null"
        seats[row][col].cost = 0.0
        seats[row][col].sold = False

print(seats)