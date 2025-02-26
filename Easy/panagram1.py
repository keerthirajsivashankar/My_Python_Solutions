def is_pangram(s):
    s = s.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s))

s = input("Enter the string: ")
print(is_pangram(s))