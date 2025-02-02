from collections import Counter
s1 = input("Enter the string1 : ")
s2 = input("Enter the string2 : ")
s1 = Counter(s1)
s2 = Counter(s2)
print(s1 == s2)