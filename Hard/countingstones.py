def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    S = int(data[0])
    R = int(data[1])
    
    sample_sizes = list(map(int, data[2:2+S]))
    ranges = []
    index = 2 + S
    for _ in range(R):
        low = int(data[index])
        high = int(data[index+1])
        ranges.append((low, high))
        index += 2
    
    # Step 1: Frequency array for sample sizes (1 to 1000)
    freq = [0] * 1001
    for size in sample_sizes:
        freq[size] += 1
    
    # Step 2: Prefix sum of frequencies
    prefix = [0] * 1001
    prefix[0] = freq[0]
    for i in range(1, 1001):
        prefix[i] = prefix[i-1] + freq[i]
    
    # Step 3: Answer each range using prefix sum
    for low, high in ranges:
        if low == 0:
            print(prefix[high])
        else:
            print(prefix[high] - prefix[low - 1])

if __name__ == "__main__":
    main()
