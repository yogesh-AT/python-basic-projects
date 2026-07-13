numbers = [4,7,2,4,8,7,9,2,10]
newlist = []
#using loops
for number in numbers:
    if number not in newlist:
        newlist.append(number)
print(newlist)