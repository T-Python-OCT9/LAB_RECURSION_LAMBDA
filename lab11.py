
# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4




def vow(pharse : str)-> int:
    vowels = 'aeiou'
    count = 0
    if len(pharse) == 0:
        return 0
    if pharse[0].lower() in vowels:
        count+= 1
    return count + vow(pharse[1:])

print(vow("i love python"))
    







# 2) Given a list of numbers : [40,35, 10, 15, 20]
# create a new list containing each number from the previous list mutliplied by itself.
# print the new list.
# Hint: use map() with a lambda funciton



my_list = [40, 35, 10, 15, 20]
my_mul_list = list(map(lambda item : item*item, my_list ))

print(my_mul_list)







