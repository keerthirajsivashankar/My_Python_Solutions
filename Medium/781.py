import collections

class Solution:
  def numRabbits(self, answers: list[int]) -> int:
    """
    Calculates the minimum number of rabbits in the forest based on their answers.

    Args:
        answers: A list of integers representing the answers given by rabbits
                 about the number of other rabbits with the same color as them.

    Returns:
        The minimum total number of rabbits in the forest.
    """
    ans = 0
    count = collections.Counter()

    for answer in answers:
      if count[answer] == 0:
        ans += answer + 1
        count[answer] = 1
      else:
        count[answer] += 1
        if count[answer] == answer + 1:
          count[answer] = 0

    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  answers1 = [1, 1, 2]
  print(f"Minimum rabbits for answers {answers1}: {sol.numRabbits(answers1)}")

  answers2 = [10, 10, 10]
  print(f"Minimum rabbits for answers {answers2}: {sol.numRabbits(answers2)}")

  answers3 = []
  print(f"Minimum rabbits for answers {answers3}: {sol.numRabbits(answers3)}")

  answers4 = [0, 0, 0]
  print(f"Minimum rabbits for answers {answers4}: {sol.numRabbits(answers4)}")

  answers5 = [1, 0, 1]
  print(f"Minimum rabbits for answers {answers5}: {sol.numRabbits(answers5)}")

  answers6 = [2, 1, 2, 1, 2]
  print(f"Minimum rabbits for answers {answers6}: {sol.numRabbits(answers6)}")