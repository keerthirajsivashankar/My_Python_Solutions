def smallest_lexicographical_string(P, S):
    # Create a mapping of characters to their order in P
    order_dict = {P[i]: i for i in range(len(P))}

    # Sort string S using the order specified in P
    sorted_S = sorted(S, key=lambda char: order_dict[char])

    # Convert the sorted list back to a string
    result = ''.join(sorted_S)
    
    return result

# Number of test cases
T = int(input())
results = []

# Process each test case
for _ in range(T):
    # Read P and S for each test case
    P = input()
    S = input()
    
    # Get the smallest lexicographical string
    result = smallest_lexicographical_string(P, S)
    results.append(result)

# Print all results
for res in results:
    print(res)
