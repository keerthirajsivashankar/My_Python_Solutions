s = input("Enter the String : ")
i = 0
j = len(s)-1
v = True
while(i<j):
    if(s[i] != s[j]):
        v = False
        break
    else:
        i += 1
        j -= 1
if(v):
    print("Yes it is a palindrome")
else:
    print("No it is not")