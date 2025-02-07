l = list(map(int, input("Enter numbers separated by commas: ").split(",")))
num_set = set(l)  
max_length = 0

for num in num_set:
    if num - 1 not in num_set:  
        current_num = num
        current_length = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_length += 1

        max_length = max(max_length, current_length)

print("Longest Consecutive Sequence Length:", max_length)
