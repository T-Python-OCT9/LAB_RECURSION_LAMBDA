def cont( x : str) -> str :
    if len(x) == 0:
        return 0
    lower_x = x.lower()
    character = lower_x[0]
    if character in 'aeiou':
        return 1 + cont((lower_x[1:]))
    return cont((lower_x[1:]))
print(cont("I love python"))

print(list(map(lambda n: n * n, [40,35, 10, 15, 20])))