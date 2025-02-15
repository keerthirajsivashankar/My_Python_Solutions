def isvalid(s):
    close_to_open = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    stack = []
    for brackets in s :
        if brackets in close_to_open:
            if not stack:
                return False
            top = stack.pop()
            if close_to_open[brackets] != top:
                return False
        else:
            stack.append(brackets) 
    if stack:
        return False
    else:
        return True
s = input()
print(isvalid(s))