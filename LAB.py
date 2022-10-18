def count_vowels(phrase : str) -> int:
    '''This Function Take a Pharase And Return The Number Of Vowels Characters '''
    count : int = 0    # define a variable to count the vowels characters
    if len(phrase) == 0:   # base condition 
        return count
    print(f'the phrase now is: {phrase}')   # print the phrase just to be clear
    if phrase[0].lower() in 'aeiou':    # check if first char in phrase is vowels
        count =+1   # add 1 to count if it is true
    return count + count_vowels(phrase[1:])   # call the function again but from index 1

result = count_vowels('i love python')
print(f'The Number Of the Vowels Characters is: {result}')


# create a new list containing each number from the previous list mutliplied by itself
print(list(map(lambda num: num * num,[40,35, 10, 15, 20])))
