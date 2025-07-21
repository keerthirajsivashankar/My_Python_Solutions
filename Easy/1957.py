class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            if len(stack) >= 3:
                if stack[-1] == stack[-2] == stack[-3]:
                    stack.pop()

        return "".join(stack)

def get_string_input(prompt: str) -> str:
    return input(prompt)

if __name__ == "__main__":
    sol = Solution()
    
    s_val = get_string_input("Enter the string: ")

    result = sol.makeFancyString(s_val)
    print(f"The fancy string is: {result}")