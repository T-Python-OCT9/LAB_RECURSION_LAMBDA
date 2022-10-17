def vowelsNumber(word:str)->int:

    if len(word)==0:
        return 0


    vowels ='aeiuo'
    count=0
    if word[0].lower() in vowels:
            count+=1
           
    return count+vowelsNumber(word[1:])
    
   


print(vowelsNumber("I love python"))





numbers=[40,35,10,15,20]
list_numbers=map(lambda number: number*number,numbers)
print(list(list_numbers))










