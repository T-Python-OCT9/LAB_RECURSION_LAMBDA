'''
LAB_RECURSION_LAMBDA
'''
## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def vowels( word : str) -> str :
    if len(word) == 0:
        return 0
    chWord = word.lower()
    character = chWord[0]
    if character in 'aeiou':
        print(character) # just to print all vowles in the word
        return 1 + vowels(chWord[1:]) 
    return vowels(chWord[1:]) 

print(vowels("I love python"))





## 2) create a new list containing each number from the previous list mutliplied by itself.
print(list(map(lambda n: n * n, [40,35, 10, 15, 20])))