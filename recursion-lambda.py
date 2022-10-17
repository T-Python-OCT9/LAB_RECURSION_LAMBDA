#1
def vowel_count(text):
    count = 0 
    vowels ="aeiouAEIOU"

    if not text:
        return 0

    if text[0] in vowels:
        return 1 + vowel_count(text[1:])

    return vowel_count(text[1:]) 
test_text: str=input("please enter the phrase te count vowels letter:\n")

result=vowel_count(test_text)
print(f"numbers of vowels in\t{test_text}\t is {result}\t")


def vowel_count(text):
    count = 0 
    vowels ="aeiouAEIOU"

    if not text:
        return 0

    if text[0] in vowels:
        return 1 + vowel_count(text[1:])

    return vowel_count(text[1:]) 
#2
number_list=[40,35,10,15,20]
new_list=list(map(lambda x : x*x,number_list))
print(new_list)
