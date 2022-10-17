def find_vowels(text : str):
    if len(text) == 0:
        return 0
    phrase = text.lower()
    char = phrase[0]
    if char in 'aeiou':
        return 1 + find_vowels(phrase[1:])
    return find_vowels(phrase[1:])

print(find_vowels('i love python'))

# create a new list containing each number from the previous list mutliplied by itself
print(list(map(lambda num: num * num,[40,35, 10, 15, 20])))

