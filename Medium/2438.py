import ast

class Solution:
  """
  A class to solve the product queries problem.
  """
  def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
    """
    Calculates the product of powers of two for given query ranges.

    The method first finds all the powers of two that sum up to 'n'.
    It then iterates through each query, calculates the product of the
    powers of two in the specified range, and returns the result
    modulo 1,000,000,007.

    Args:
      n: The initial integer.
      queries: A list of lists, where each inner list [left, right]
               represents the start and end indices for the product.

    Returns:
      A list of integers, where each integer is the product for a query.
    """
    MOD = 1_000_000_007
    MAX_BIT = 30  # Max power of 2 for n <= 10^9 is 2^29

    # This finds the powers of two that make up 'n'.
    # `n >> i & 1` checks if the i-th bit is set.
    # `1 << i` calculates 2^i.
    pows = [1 << i for i in range(MAX_BIT) if n >> i & 1]

    ans = []
    
    # Iterate through each query (left, right).
    for left, right in queries:
      prod = 1
      # Calculate the product for the specified range.
      for i in range(left, right + 1):
        prod *= pows[i]
        prod %= MOD
      ans.append(prod)

    return ans

if __name__ == "__main__":
    try:
        # Get user input for 'n'
        n_input = input("Enter a non-negative integer (n): ")
        n = int(n_input)
        
        # Get user input for 'queries' as a list of lists.
        queries_input = input("Enter queries as a list of lists (e.g., [[0,1],[2,2]]): ")
        queries = ast.literal_eval(queries_input)

        # Create an instance of the Solution class.
        solution = Solution()
        
        # Call the method and print the result.
        result = solution.productQueries(n, queries)
        
        print(f"The results of the product queries are: {result}")
        
    except (ValueError, SyntaxError) as e:
        print(f"Invalid input: {e}")
        print("Please ensure your input for 'n' is an integer and 'queries' is a valid list of lists.")

