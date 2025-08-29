class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculates the number of winning combinations for Alice in the Flower Game.
        
        Alice wins if the sum of her chosen number (x) and Bob's chosen
        number (y) is odd. This occurs when one number is even and the other
        is odd.

        Args:
            n: The number of flowers Alice can choose from.
            m: The number of flowers Bob can choose from.

        Returns:
            The total number of winning combinations.
        """
        # Calculate the number of even and odd flowers for Alice (n)
        x_even = n // 2
        x_odd = (n + 1) // 2

        # Calculate the number of even and odd flowers for Bob (m)
        y_even = m // 2
        y_odd = (m + 1) // 2

        # The total winning combinations are:
        # (Alice picks even * Bob picks odd) + (Alice picks odd * Bob picks even)
        return x_even * y_odd + x_odd * y_even

# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print("--- Welcome to the Flower Game! ---")
    
    # Get user input for n
    while True:
        try:
            n_input = int(input("Enter the number of flowers Alice has (n): "))
            if n_input >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    # Get user input for m
    while True:
        try:
            m_input = int(input("Enter the number of flowers Bob has (m): "))
            if m_input >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    result = sol.flowerGame(n_input, m_input)
    print(f"\nThere are a total of {result} winning combinations.")