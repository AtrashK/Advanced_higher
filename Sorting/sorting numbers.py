import random

numbers = [random.randint(1,10) for i in range(10)]

for i in range(len(numbers)-1):
    j=0
    switched=True
    while (switched and j<=i):
        current_number=numbers[i+1-j]
        previous_number=numbers[i-j]
        if (current_number<previous_number):
            numbers[i-j]=current_number
            numbers[i+1-j]=previous_number
            j+=1
        else:
            switched=False
    
print(numbers)