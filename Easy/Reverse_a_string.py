s = input("Enter the string : ")
s.strip()
s = list(s)
i,j = 0 , len(s)-1
while(i < j):
    s[i],s[j] = s[j],s[i]
    i+=1
    j-=1
print("".join(s))