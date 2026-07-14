print('enter any word')
word = input()
listword = list(word)
dictionery = {}
for letter in listword:
    if letter in dictionery:
      dictionery[letter] += 1
    else :
        dictionery[letter] = 1
print(dictionery)

for i in dictionery:
    print(i, dictionery[i])