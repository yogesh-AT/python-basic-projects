print('give any number')
num = input()
listnum = list(num)
power = len(listnum)
k = 0
for i in range(0,power):
    new = int(listnum[i]) ** power
    k = k + new
if k == int(num):
    print('the given number is a armstrong number')
else :
        print('the given number is not a armstrong number')