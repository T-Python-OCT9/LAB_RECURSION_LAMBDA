def vowels_cont( x : str) -> str :
    if len(x) == 0:
        return 0
    lower_x = x.lower()
    character = lower_x[0]
    if character in 'aeiou':
        print(character)
        return 1 + vowels_cont((lower_x[1:]))
    return vowels_cont((lower_x[1:]))

print(vowels_cont("python"))

print(list(map(lambda n: n * n, [40,35, 10, 15, 20])))
