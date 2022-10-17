'''
# LAB_RECURSION_LAMBDA


## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4 


## 2) Given a list of numbers : [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

'''

#First question

def numofVowel(user_input):
    
    if user_input == "":
        return 0 
    elif user_input[0] in "aeiouAEIOU":
        return 1 + numofVowel(user_input[1:])    
    else: 
        return 0 + numofVowel(user_input[1:])    


print(numofVowel(str(input("Enter a text : "))))


#Second Question


number_list = [40,35, 10, 15, 20]


print(list(map(lambda n: n*n, number_list)))


