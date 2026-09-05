def initialise():
    searchlist = [1,3,5,7,9,11,13,17,18,19,21]
    print("Original list:",searchlist)
    return searchlist


def BinarySearch(searchlist, goal):
    found = False
    startpos = 0
    endpos = len(searchlist) -1
    comparisons =0

    print("Endpos at beginning = ",endpos)


    while (startpos <= endpos) and found == False:
        middle = (startpos+endpos)//2 #Integer Division
        if searchlist[middle] == goal:
            found = True
        elif searchlist[middle]<goal:
            startpos = middle + 1
        else:
            endpos = middle -1
        comparisons+=1

    if (found==False):
        middle=-1

    print(str(comparisons) + " comparisons were done. ")
    return middle

values = initialise()

goal = int(input("Enter goal "))
print(BinarySearch(values,goal))


# 3 4 1 4