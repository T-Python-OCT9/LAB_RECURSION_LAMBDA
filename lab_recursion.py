# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def vowelsCheck(text: str):
    if text == '':
        return 0
    elif text[0].upper() in ['A', 'E', 'I', 'O', 'U']:
        return 1 + vowelsCheck(text[1:])
    else:
        return 0 + vowelsCheck(text[1:])


print(vowelsCheck("I love python"))


# 2) Given a list of numbers : [40,35, 10, 15, 20]
# create a new list containing each number from the previous list mutliplied by itself.
numbers_list = [40, 35, 10, 15, 20]
multiplied_number = list(map(lambda item: item * item, numbers_list))
print(multiplied_number)
