def string(s):
    if len(s) == 0:
        return None
    v = ["a","e","i","o","u","A","E","I","O","U"]
    v = set(v)
    i , j = 0 , len(s) - 1
    s = list(s)
    while i < j :
        if s[i] in v and s[j] in v:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        elif s[i] in v and s[j] not in v:
            j -= 1
        elif s[i] not in v and s[j] in v:
            i += 1
        else:
            i += 1
            j -= 1
    return ("".join(s))
#driver code
s = input("Enter the string : ")
print(string(s))