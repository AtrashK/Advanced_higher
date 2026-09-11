myList = ["G","X","b","P","z"]

#start from the right
for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        #compare two adjacent values
        if ord(myList[inner])>ord(myList[inner+1]):
            myList[inner], myList[inner+1] = myList[inner+1], myList[inner]
  
print("Bubble sort complete")
print(myList)
