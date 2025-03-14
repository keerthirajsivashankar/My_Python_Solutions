def maximum_candies(candies: list[int], k: int) -> int:
    """
    Finds the maximum number of candies each child can get.

    Args:
        candies: A list of integers representing the number of candies in each pile.
        k: The number of children.

    Returns:
        The maximum number of candies each child can get.
    """
    l = 1
    r = sum(candies) // k

    def num_children(m: int) -> int:
        """Calculates how many children can get 'm' candies."""
        return sum(c // m for c in candies)

    while l < r:
        m = (l + r + 1) // 2 # changed to ceiling division to prevent infinite loops
        if num_children(m) < k:
            r = m - 1 # changed to m - 1 to make it correct
        else:
            l = m

    return l if num_children(l) >= k else l - 1

# Driver Code
if __name__ == "__main__":
    # Example usage:
    candies1 = [5, 8, 6]
    k1 = 3
    result1 = maximum_candies(candies1, k1)
    print(f"Maximum candies for {candies1}, {k1}: {result1}")

    candies2 = [1, 2, 3, 4, 5]
    k2 = 10
    result2 = maximum_candies(candies2, k2)
    print(f"Maximum candies for {candies2}, {k2}: {result2}")

    candies3 = [10,10]
    k3 = 1
    result3 = maximum_candies(candies3, k3)
    print(f"Maximum candies for {candies3}, {k3}: {result3}")

    candies4 = [10,10]
    k4 = 2
    result4 = maximum_candies(candies4, k4)
    print(f"Maximum candies for {candies4}, {k4}: {result4}")

    candies5 = [10,10]
    k5 = 3
    result5 = maximum_candies(candies5, k5)
    print(f"Maximum candies for {candies5}, {k5}: {result5}")

    candies6 = [10,10]
    k6 = 20
    result6 = maximum_candies(candies6, k6)
    print(f"Maximum candies for {candies6}, {k6}: {result6}")