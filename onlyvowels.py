print('give any word')
#Convert all the letters into lower case
word = input().lower()
listword = list(word)
#create a empty list and append only vowels in it using loops
vowelsinlist = []
for i in range(len(listword)):
    if (listword[i] == 'a' or listword[i] == 'e' or listword[i] == 'i'
            or listword[i] == 'o' or listword[i] == 'u'):
     vowelsinlist.append(listword[i])
    continue

set = set(vowelsinlist)
print('the vowels in this word are:')
print(set)

