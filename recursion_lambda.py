# LAB_RECURSION_LAMBDA
# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def find_vowels(i):
    if not i:
        return 0
    if i[0].lower() in 'aeiou':
        count = 1
    else:
        count = 0
    return count + find_vowels(i[1:])


print(find_vowels("I love python"))

# 2) Given a list of numbers : [40,35, 10, 15, 20]
listone = [40, 35, 10, 15, 20]
# create a new list containing each number from the previous list mutliplied by itself.
mutliplied_list = [element * element for element in listone]
print(list(mutliplied_list))
# print the new list.
# Hint: use map() with a lambda funciton
mutliplied_list1 = map((lambda x: x*x), listone)
print(list(mutliplied_list1))
  