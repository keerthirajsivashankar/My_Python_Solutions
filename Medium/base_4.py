def base_negative_4(n: int) -> str:
    if n == 0:
        return "0"

    result = ""
    while n != 0:
        remainder = n % -4
        n = n // -4

        if remainder < 0:
            remainder += 4
            n += 1

        result += str(remainder)

    return result[::-1]
#driver code 
n = int(input("Enter the number : "))
print(base_negative_4(n))