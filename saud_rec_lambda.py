def find_vowels(word , count=0):
    if word:
        if word[0] in ("a","e","i","o","u","A","E","I","O","U"):
            count += 1
        return find_vowels(word=word[1:], count=count)
    else:
     return count 
print(find_vowels("i love python"))   
  
list_numbers = [40,35,10,15,20] 
print("the new list mutliplied by itself")
print(list(map(lambda numberser:numberser*numberser,list_numbers)))

