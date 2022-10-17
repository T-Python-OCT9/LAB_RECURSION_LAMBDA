## 1 ##

def Vowels(vowel):
	return vowel in ['A', 'E', 'I', 'O', 'U' , 'a' , 'e' , 'i' , 'o' , 'u']

txt = input("please entre a word to count the vowels:")

def num_of_vowels(txt :str, coun)->int:
	if (coun == 1):
		return Vowels(txt[coun - 1])
    
	else:
         return (num_of_vowels(txt, coun - 1) +
				Vowels(txt[coun - 1]))


print(num_of_vowels(txt, len(txt)))

## 2 ##
list1=[40,35, 10, 15, 20]
multiply_list = map(lambda x:x*x , list1)
print("new multiply List:",list(multiply_list))