
VOWELS = 'aeiouAEIOU'

def count_vowels(s):
    if not s:
        return 0
    return int(s[0] in VOWELS) + count_vowels(s[1:])


print (count_vowels("i love python"))



my_list = [40,35, 10, 15, 20]
multiplying_list_items =  (map(lambda i : i * i, my_list))
print (list(multiplying_list_items))


