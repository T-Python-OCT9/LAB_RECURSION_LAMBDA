# LAB_RECURSION_LAMBDA


## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4 


## 2) Given a list of numbers : [40,35, 10, 15, 20]


def find_vowels(x : str):
    vowels_list = ["a", "e", "o","i","u"]
    for i in vowels_list :
        if i in vowels_list:
          vowels= list()
          result= str(vowels.append(i))
          
        else:
             continue
        return result

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton
