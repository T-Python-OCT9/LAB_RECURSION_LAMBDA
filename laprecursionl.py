#LAB_RECURSION_LAMBDA


## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
#def vowls ():
'''
def vowls( i: str ) -> int :
    if len(i) ==0:
        return 0 
    count = 0
    if i in 'aeiou':
        count +=1
        vowls(i)
    else:
        
        return vowls(i)
        return count

#w =  ["l","o","v","e"]
print(vowls("LOVe"))
'''
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
# Returns count of vowels in str 
def countVowels(str):
    count = 0
    # for i in range(len(str)):
 
        # Check for vowel
    if isVowel(str[i]):
        count += 1
    return count , countVowels(str , i+1 )

str = 'love '
 

print(countVowels(str))


#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4 


#2) Given a list of numbers : [40,35, 10, 15, 20]

num_list =[40,35, 10, 15, 20]
#sumNum = list(filter(lambda e : e*e , num_list ))
sumNum =  list (map (lambda x: x * x , num_list))

print("is : " , sumNum) 
#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton
