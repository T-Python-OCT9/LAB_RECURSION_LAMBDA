
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
# to count total number of
# vowel from 0 to n
def countVovels(str, n):
    if (n == 1):
        return isVowel(str[n - 1])
 
    return (countVovels(str, n - 1) +
                isVowel(str[n - 1]))
 

 
# string object
str = "i love python I LOVE PYTHON"
 
# Total numbers of Vowel
print(countVovels(str, len(str)))


number_list = [40,35, 10, 15, 20]

print (list(map (lambda n: n*n, number_list)))

