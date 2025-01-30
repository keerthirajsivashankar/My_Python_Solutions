s = input("Enter the string : ")
v = "aeiouAEIOU"
co = 0
if len(s) == 0:
    print("Enter the string,please")
else:
    for c in s:
        if c in v:
            co += 1
if co > 0 :
    print(f"The number of Vowels is : {co}")
else:
    print("their are no vowels")