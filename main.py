## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def VowelCount(s):
    ''' this function will take the input and check if it has a vowels in it and retrun the number of how many the string have in '''
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    elif s[0] in vowels:
        return 1 + VowelCount(s[1:])
    else:
        return 0 + VowelCount(s[1:])

print("This statment (Ilove python) has in it : ",VowelCount("iLOve python"),"vowels in it .")

# create a new list containing each number from the previous list mutliplied by itself.
 
multiply_list = [40,35, 10, 15, 20] 

multiply_result = list(map(lambda nums : nums*nums ,multiply_list))

print("The result of multply the list is : ",multiply_result) 