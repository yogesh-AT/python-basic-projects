
num = []
num.append(0)
num.append(1)
for i in range(2,1000):
    new =num[i-1]+num[i-2]
    num.append(new)
print(num)