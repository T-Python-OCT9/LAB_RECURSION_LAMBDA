from unittest import result

def Rec_find_vowels(text:str):
    vowels_list = "aeoiuAIOUE"
    counter=0
    if not text:
        return 0
    
    if text[0] in vowels_list:
        return 1 + Rec_find_vowels(text[1:])
    return Rec_find_vowels(text[1:])

Rec_find_vowels("munira")
