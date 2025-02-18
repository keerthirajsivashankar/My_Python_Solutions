def remove_adjacent_duplicates(s):
    stack = []
    
    for char in s:
        # If the stack is not empty and the top element is the same as the current character, remove it
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)

# Input
s = input("Enter the string: ")
print("Result:", remove_adjacent_duplicates(s))
