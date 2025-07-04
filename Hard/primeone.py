def infix_to_postfix(expression):
    result = []
    my_stack = []
    
    for char in expression:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            result.append(char)
        elif char == '(':  # If character is '(', push it onto the stack
            my_stack.append(char)
        elif char == ')':  # If character is ')'
            while my_stack and my_stack[-1] != '(':  # Pop until '(' is found
                result.append(my_stack.pop())
            if my_stack:  # Pop the '(' from the stack
                my_stack.pop()
        else:  # If the character is an operator
            my_stack.append(char)
    
    # Pop all the operators from the stack
    while my_stack:
        result.append(my_stack.pop())
    
    return ''.join(result)

def main():
    t = int(input())
    for _ in range(t):
        expression = input()
        print(infix_to_postfix(expression))

if __name__ == "__main__":
    main()