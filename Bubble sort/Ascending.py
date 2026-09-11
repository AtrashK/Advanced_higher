myList = [3,4,9,7,1]

#start from the right
for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        #compare two adjacent values
        if myList[inner]>myList[inner+1]:
            myList[inner], myList[inner+1] = myList[inner+1], myList[inner]
  
print("Bubble sort complete")
print(myList)
