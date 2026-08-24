class ticket:
    def __init__(self): # constructor
        self.movie_name = "Spiderman"
        self.date = "01/01/2026"
        self.time = "01:00"
        self.name = "Zeus"

    def setMovieName(self, thisMovieName): # setter
        self.movie_name = thisMovieName

    def getMovieName(self):
        return self.movie_name

    def setDate(self, thisDate): # setter
        self.date = thisDate

    def getDate(self):
        return self.date

    def setTime(self, thisTime): # setter
        self.time = thisTime

    def getTime(self):
        return self.time

    def setName(self, thisName): # setter
        self.name = thisName

    def getName(self):
        return self.name

customers = [ticket() for index in range(5)]

customers[0].setMovieName("Inside Out 2")
customers[0].setDate("02/02/2026")
customers[0].setTime("19:00")
customers[0].setName("Lol")

print(customers[0].getMovieName())
print(customers[0].getDate())
print(customers[0].getTime())
print(customers[0].getName())

print(customers[1].getMovieName())
print(customers[1].getDate())
print(customers[1].getTime())
print(customers[1].getName())
