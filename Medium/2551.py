import heapq
import itertools

def put_marbles(weights: list[int], k: int) -> int:
    """
    Calculates the difference between the maximum and minimum score of dividing marbles into k bags.

    Args:
        weights: A list of integers representing the weights of marbles.
        k: The number of bags.

    Returns:
        The difference between the maximum and minimum score.
    """
    arr = [a + b for a, b in itertools.pairwise(weights)]
    return sum(heapq.nlargest(k - 1, arr)) - sum(heapq.nsmallest(k - 1, arr))

if __name__ == "__main__":
    weights1 = [1, 3, 5, 1]
    k1 = 2
    result1 = put_marbles(weights1, k1)
    print(f"Marbles for {weights1}, {k1}: {result1}")

    weights2 = [1, 3, 5, 1]
    k2 = 3
    result2 = put_marbles(weights2, k2)
    print(f"Marbles for {weights2}, {k2}: {result2}")

    weights3 = [1, 3, 5, 1]
    k3 = 4
    result3 = put_marbles(weights3, k3)
    print(f"Marbles for {weights3}, {k3}: {result3}")

    weights4 = [10, 1, 6, 2, 7, 3, 4]
    k4 = 4
    result4 = put_marbles(weights4, k4)
    print(f"Marbles for {weights4}, {k4}: {result4}")

    weights5 = [1]
    k5 = 1
    result5 = put_marbles(weights5,k5)
    print(f"Marbles for {weights5}, {k5}: {result5}")

    weights6 = [1,2]
    k6 = 2
    result6 = put_marbles(weights6,k6)
    print(f"Marbles for {weights6}, {k6}: {result6}")