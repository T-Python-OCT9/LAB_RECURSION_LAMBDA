import math
#Q1
def vow(v):
    #using loop
    '''if len(v) == 0:
      return'''
           
    '''for v in text:
        if v == "o" or v == "i" or v == "e" or v == "a" or v == "u" or v == "O" or v == "I" or v == "E" or v == "A" or v == "U":
          counter = counter + 1'''

    #using recursion
    list_v = list("o","i","u","e","a")
    counter : int 
    for y in list_v:
        if v == y:
          counter = counter + 1
          return vow(v)

    print(counter)
   
text = "I love python"
print(vow(text))          

#Q2  
list1 = [40,35, 10, 15, 20]
list2 = map(lambda num : num*num , list1 )
print(list(list2))

