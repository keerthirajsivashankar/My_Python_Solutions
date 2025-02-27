from collections import Counter

def second(s):
    count = Counter(s)
    
    # Get unique frequencies in descending order
    freqs = sorted(set(count.values()), reverse=True)
    
    if len(freqs) < 2:  
        return None  # No second most frequent character  
    
    second_most_freq = freqs[1]  # Second highest frequency  
    
    for k, v in count.items():
        if v == second_most_freq:
            return k  # Return the first character with second highest frequency  

s = input("Enter the string: ")
print(second(s))
