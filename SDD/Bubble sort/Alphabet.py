<<<<<<< HEAD
myList = ["p","o","r","t","y"]
=======
myList = ["G","X","b","P","z"]
>>>>>>> c23bdcfff07fe160f32ba9ded4aec9df6ecab5d9

#start from the right
for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        #compare two adjacent values
        if ord(myList[inner])>ord(myList[inner+1]):
            myList[inner], myList[inner+1] = myList[inner+1], myList[inner]
  
print("Bubble sort complete")
print(myList)
<<<<<<< HEAD

=======
>>>>>>> c23bdcfff07fe160f32ba9ded4aec9df6ecab5d9
