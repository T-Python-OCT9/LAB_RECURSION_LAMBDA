


def number_vowels(word : str) -> int:
    if len(word) == 0 :
        return 0

    vowels = "aeiou"
    count = 0
    if word[0].lower() in vowels:
        count += 1
    return count + number_vowels(word[1:])




print(number_vowels("I love python"))



numbers_11 = [40,35, 10, 15, 20]
mutliplied =   list(map(lambda item : item*item, numbers_11))
print(mutliplied)