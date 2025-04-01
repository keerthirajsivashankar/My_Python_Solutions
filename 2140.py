def most_points(questions: list[list[int]]) -> int:
    """
    Calculates the maximum points obtainable by answering questions.

    Args:
        questions: A list of questions, where each question is [points, brainpower].

    Returns:
        The maximum points obtainable.
    """
    n = len(questions)
    dp = [0] * (n + 1)

    for i in reversed(range(n)):
        points, brainpower = questions[i]
        next_index = i + brainpower + 1
        next_points = dp[next_index] if next_index < n else 0
        dp[i] = max(points + next_points, dp[i + 1])

    return dp[0]

if __name__ == "__main__":
    questions1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
    result1 = most_points(questions1)
    print(f"Most points for {questions1}: {result1}")

    questions2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    result2 = most_points(questions2)
    print(f"Most points for {questions2}: {result2}")

    questions3 = [[1,0],[2,0],[3,0],[4,0],[5,0]]
    result3 = most_points(questions3)
    print(f"Most points for {questions3}: {result3}")

    questions4 = [[100,100],[1,1],[1,1],[1,1],[1,1]]
    result4 = most_points(questions4)
    print(f"Most points for {questions4}: {result4}")
    questions5 = [[10,1],[1,10],[10,1]]
    result5 = most_points(questions5)
    print(f"Most points for {questions5}: {result5}")

    questions6 = [[5,0]]
    result6 = most_points(questions6)
    print(f"Most points for {questions6}: {result6}")

    questions7 = []
    result7 = most_points(questions7)
    print(f"Most points for {questions7}: {result7}")