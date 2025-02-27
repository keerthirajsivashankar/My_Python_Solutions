from collections import Counter
def frequencyofstring(string):
    frequency = Counter(string)
    max_count = 0
    count_character = string[0]
    for key,value in frequency.items():
        if value > max_count:
            max_count = value
            count_character = key
    return count_character
#driver Code
string = input("Enter the string : ") 
print(frequencyofstring(string))   