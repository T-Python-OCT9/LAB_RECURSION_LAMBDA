## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def count_vowels(text:str)-> int:
    count = 0
    for i in range(len(text)):
 
        # Check for vowel
        if isVowel(text[i]):
            count += 1
    return count

Text = str (input("Enter your text:  "))

print("The vowels number is:  ", count_vowels(Text))





