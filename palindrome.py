

print('give any word')
word = input()
#convert the string into list to divide it into individual letters
listword = list(word)
print(listword)
n = 0
palindromeyes = True
#nth letter from beginning and from end are same  
#But in progamme beggining 'n'starts with 0  
while n < len(listword)/2 :
    if listword[n] != listword[-(n+1)]  :
        palindromeyes = False
        break
    n += 1

if palindromeyes :
        print('the word is palindrome')
else:
        print('the word is not palindrome')