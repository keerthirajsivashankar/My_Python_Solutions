def max_complete_layers(N):
    left, right = 0, N  
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total_bricks = mid * (mid + 1) // 2  

        if total_bricks <= N:
            result = mid  
            left = mid + 1  
        else:
            right = mid - 1  

    return result

def main():
    T = int(input(""))

    for _ in range(T):
        N = int(input(" "))
        print(max_complete_layers(N))

if __name__ == "__main__":
    main()
