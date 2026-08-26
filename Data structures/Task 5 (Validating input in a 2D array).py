seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'


seat_allocated=False
initials = input("Please enter your initials ")
while (not seat_allocated):
    row = int(input("Please enter your seat row "))
    col = int(input("Please enter your seat coloumn "))

    if (row>1 or row<0 or col>4 or col<0):
        print("That is not a valid seat row and column")
    elif (seat[row][col]!=""):
        print("That seat has already been filled. Please choose another seat.")
    else:
        print("Thank you. Your seat has been allocated. ")
        seat_allocated=True
        seat[row][col]=initials

for row in range(2):
    print(seat[row])

