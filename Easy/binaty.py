def is_valid_partition(boards, k, max_length):
    painters_required = 1
    current_length = 0

    for length in boards:
        if current_length + length > max_length:
            painters_required += 1
            current_length = length
            if painters_required > k:
                return False
        else:
            current_length += length
    return True

def painter_partition(boards, k):
    low = max(boards)
    high = sum(boards)
    result = high

    while low <= high:
        mid = (low + high) // 2

        if is_valid_partition(boards, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

# Input and Output using input()
def main():
    t = int(input())  
    results = []  

    for _ in range(t):
        N, k = map(int, input().split())  
        boards = list(map(int, input().split())) 
        results.append(str(painter_partition(boards, k))) 
    print("\n".join(results))

if __name__ == "__main__":
    main()
