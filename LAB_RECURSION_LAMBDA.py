'''
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .

Example: given the phrase "I love python" , it should return : 4

'''

def vowels(x):
    return x.upper() in ['A', 'E', 'I', 'O', 'U']


def countVovels(str, n):
    if (n == 1):
        return vowels(str[n - 1]);
    return (countVovels(str, n - 1) +
            vowels(str[n - 1]));


str = "razan a e i o u, I love python";
print(countVovels(str, len(str)))


'''
2) Given a list of numbers : [40,35, 10, 15, 20]

create a new list containing each number from the previous list mutliplied by itself.

print the new list.

Hint: use map() with a lambda funciton

'''

list_number = [40,35, 10, 15, 20]
print(list(map(lambda x: x*x, list_number)))