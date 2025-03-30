def partition_labels(s: str) -> list[int]:
    """
    Partitions a string into as many parts as possible so that each letter appears in at most one part.

    Args:
        s: The input string.

    Returns:
        A list of integers representing the size of these parts.
    """
    ans = []
    letter_to_rightmost_index = {c: i for i, c in enumerate(s)}

    l = 0  # the leftmost index of the current running string
    r = 0  # the rightmost index of the current running string

    for i, c in enumerate(s):
        r = max(r, letter_to_rightmost_index[c])
        if i == r:
            ans.append(r - l + 1)
            l = r + 1

    return ans

if __name__ == "__main__":
    s1 = "ababcbacadefegdehijhklij"
    result1 = partition_labels(s1)
    print(f"Partition labels for {s1}: {result1}")

    s2 = "eccbbbeffedc"
    result2 = partition_labels(s2)
    print(f"Partition labels for {s2}: {result2}")

    s3 = "abcdefg"
    result3 = partition_labels(s3)
    print(f"Partition labels for {s3}: {result3}")

    s4 = "aaaaa"
    result4 = partition_labels(s4)
    print(f"Partition labels for {s4}: {result4}")

    s5 = "a"
    result5 = partition_labels(s5)
    print(f"Partition labels for {s5}: {result5}")

    s6 = ""
    result6 = partition_labels(s6)
    print(f"Partition labels for {s6}: {result6}")