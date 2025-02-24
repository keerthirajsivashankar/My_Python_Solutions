from collections import Counter
def morethanone(s):
    hashmap = Counter(s)
    for key , value in hashmap.items():
        if value > 1:
            return key
    else:
        return None
s = input("Enter the string : ")
print("The first character has occured more than one : ",morethanone(s))