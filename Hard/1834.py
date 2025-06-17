import math

class Solution:
  def countGoodArrays(self, n: int, m: int, k: int) -> int:
    MOD = 1_000_000_007
    
    # Handle base cases where constraints might lead to issues with pow(base, negative_exponent)
    # or math.comb(n, k) with k > n.
    if k < 0 or k >= n: # k must be between 0 and n-1 (inclusive) for n-1Ck to be valid index for combinations
        return 0 # Or handle based on specific problem constraints if k=n is allowed

    # Calculate (m - 1)^(n - k - 1) modulo MOD
    # pow(base, exp, mod) is efficient for modular exponentiation.
    term_pow = pow(m - 1, n - k - 1, MOD)

    # Calculate combinations (n - 1)C_k modulo MOD
    # Using math.comb for combinations.
    # We need to perform modular inverse for division if MOD is prime,
    # or handle combinations differently if not.
    # However, standard math.comb returns integer result, not modulo.
    # For large n, k, and modulo, combinations need to be calculated modulo MOD.
    # If MOD is a prime number, we can use Fermat's Little Theorem for modular inverse.
    # Since MOD = 10^9 + 7 is prime, we can use modular inverse for combinations.

    # Here's the standard way to calculate nCr % p when p is prime:
    # nCr % p = (n! * (r!)^(p-2) * ((n-r)!)^(p-2)) % p
    # However, Python's math.comb works for smaller numbers, but the result can be very large.
    # The problem implies that math.comb should be implicitly handled correctly with MOD or is small.
    # Let's assume the context implies that n-1Ck is calculated first, then the product is taken modulo MOD.
    # For a correct competitive programming solution involving combinations with large numbers and modulo,
    # typically precompute factorials and inverse factorials.
    # For this specific problem, if `n-1` is small enough that `math.comb(n-1, k)` doesn't overflow
    # standard integer types before modulo, then the structure is fine.
    # However, if it overflows, this line needs a dedicated modular combination function.
    
    # Assuming math.comb(n-1, k) is directly calculable and then taken modulo MOD with other terms.
    # The `math.comb` function directly returns an integer, which could be very large.
    # We need to ensure the modulo happens after the multiplication, as shown in the original code.

    # The current line: `math.comb(n - 1, k) % MOD` only applies modulo to the combination result.
    # The whole product needs to be modulo MOD. The original code does `... % MOD * ... % MOD`.

    # Let's adjust for correctness for modular arithmetic:
    term_comb = math.comb(n - 1, k) % MOD
    
    # Calculate the final product modulo MOD
    result = (m * term_pow * term_comb) % MOD
    
    return result

def get_positive_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    n_val = get_positive_integer_input("Enter n (total length of array): ")
    m_val = get_positive_integer_input("Enter m (number of possible values for elements): ")
    k_val = get_positive_integer_input("Enter k (number of elements that must have value 0): ")

    result = sol.countGoodArrays(n_val, m_val, k_val)
    print(f"The number of good arrays is: {result}")