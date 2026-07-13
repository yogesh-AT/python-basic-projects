print('give a word :')
word = input()
listword = list(word)
reverselist = []
for i in range(len(listword)):
    reverselist.append(listword[-(i+1)])
reverseword = ''.join(reverselist)
print(reverseword)