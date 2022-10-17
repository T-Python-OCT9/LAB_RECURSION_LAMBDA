
def vowel(word :str )->int:
    if len(word)==0:
        return 0

    vowels= 'aeiou'
    count = 0
    
    if word[0].lower() in vowels:
        count+= 1
    return count + vowel(word[1:])
print(vowel("I love python"))




li = [40,35, 10, 15, 20]
 
final_list = list(map(lambda x: x*x, li))
print(list(final_list))

#li = [40,35, 10, 15, 20]
#final_list = list(map(lambda x: x*li, li))
#print(final_list)
