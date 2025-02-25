from collections import Counter

def ndmost(s):
    count = Counter(s)
    
    # Get unique frequencies in descending order
    freqs = sorted(set(count.values()), reverse=True)
    
    if len(freqs) < 2:
        return None  # No second most frequent character
    
    second_most_freq = freqs[1]  # Get the second highest frequency
    
    for char, freq in count.items():
        if freq == second_most_freq:
            return char  # Return the first character with second highest frequency

s = input("Enter the string: ")
print(ndmost(s))