def removeKdigits(num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        # Remove digits from stack if they are greater than the current digit
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        
        stack.append(digit)
    
    # Remove extra digits if `k` is still greater than 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # Convert stack to string and remove leading zeros
    result = "".join(stack).lstrip("0")
    
    # If result is empty, return "0"
    return result if result else "0"

# Example test cases
print(removeKdigits("1432219", 3))  # Output: "1219"
print(removeKdigits("10200", 1))    # Output: "200"
print(removeKdigits("10", 2))       # Output: "0"
