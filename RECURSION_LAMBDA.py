## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def count_vowels(text:str , num :int )-> int:
    count = 0

    if (num == 1):
        return isVowel(text[num - 1]);
 
    return (count_vowels(text, num - 1) + isVowel(text[num - 1]));


Text = str (input("Enter your text:  "))
print("The vowels number is:  ", count_vowels(Text,len(Text)))


## 2) Given a list of numbers : [40,35, 10, 15, 20]

List = [40,35, 10, 15, 20]
list2 = list (map(lambda x:x*x,List))

print(list2)
#print(filtered_list)


'''
lis=[1,2,3,4]
newlis = map(lambda x:x*2, lis)
print(newlis)
'''