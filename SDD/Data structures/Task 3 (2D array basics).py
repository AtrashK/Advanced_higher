rows = 4
cols = 6
seats = [['-' for c in range(cols)] for r in range(rows)]

seats[1][1]="X"
seats[2][4]="x"
seats[3][0]="X"

for i in range(rows):
    row = ""
    for j in range(cols):
        row += seats[i][j] + " "
    print(row[:-1])
 
free_seats = 0

for i in range(rows):
    for j in range(cols):
        if (seats[i][j]=="-"):
            free_seats += 1

print("There are " + str(free_seats) + " free seats.")
