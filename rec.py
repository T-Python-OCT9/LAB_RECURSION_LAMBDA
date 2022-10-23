


#1

def vowel(phrase : str):
    count=1
    if phrase == "" :
        return 0
    return (count if phrase [0] in 'aeiouAEIOU' else 0) + vowel(phrase [1:])

print(vowel("I love python"))


#2

my_list= [40,35, 10, 15, 20]

x = map(lambda a : a * a, my_list)

my_list2=list(x)

print (my_list2)