numbers = [10 , -4 , 15 , -8 , 20 , -1 , 30 ]
#create a empty list and append the positive numbers one by one
numpositive = []
for i in range(len(numbers)):
    if numbers[i] > 0:
        numpositive.append(numbers[i])
        continue
print ('positive numbers are:')
print(numpositive)