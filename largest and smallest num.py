print('how many numbers you have?')
c = input()
numbers = []
for i in range(1,int(c)+1):
    print('enter the number',i)
    value = input()
    numbers.append(int(value))

numbers.sort()
least = numbers[0]
greatest = numbers[-1]
print('greatest value is',greatest)
print('least value is',least)