from typing import List

class Solution:
  def kthSmallestProduct(
      self,
      nums1: List[int],
      nums2: List[int],
      k: int,
  ) -> int:
    # Separate negative numbers (and reverse to get ascending absolute values)
    # and non-negative numbers for both lists.
    # A1: absolute values of negative numbers from nums1, in ascending order
    # A2: non-negative numbers from nums1, in ascending order
    A1 = [-num for num in nums1 if num < 0][::-1]
    A2 = [num for num in nums1 if num >= 0]
    
    # Same for nums2
    B1 = [-num for num in nums2 if num < 0][::-1]
    B2 = [num for num in nums2 if num >= 0]

    # Calculate the total count of negative products.
    # Negative products come from (negative * positive) or (positive * negative).
    negCount = len(A1) * len(B2) + len(A2) * len(B1)

    # Determine the sign of the k-th smallest product and adjust k.
    # If k is greater than the total count of negative products, it means
    # the k-th smallest product is positive.
    if k > negCount:
      k -= negCount  # We need to find the (k - negCount)-th positive product.
      sign = 1       # The result will be positive.
    else:
      # If k is less than or equal to negCount, the k-th smallest product is negative.
      # We need to find the (negCount - k + 1)-th largest absolute value among negative products.
      # This is equivalent to finding the (negCount - k + 1)-th smallest absolute value
      # if we consider all products as positive, then negate it.
      k = negCount - k + 1
      sign = -1      # The result will be negative.
      # When finding a negative product, we want the product of (larger A * larger B) to be smaller (less negative).
      # To use the `numProductNoGreaterThan` logic which assumes positive values and ascending arrays,
      # we swap B1 and B2. This effectively means we are looking for abs(A * B) which is <= m.
      B1, B2 = B2, B1

    # Helper function to count products less than or equal to m.
    # This is used for binary search.
    def numProductNoGreaterThan(A: List[int], B: List[int], m: int) -> int:
      ans = 0
      j = len(B) - 1 # Start from the end of B (largest element)
      for i in range(len(A)):
        # For each A[i], find the largest index j such that A[i] * B[j] <= m.
        # Since B is sorted, we can move j leftwards.
        # This is a two-pointer approach (or effectively a binary search for j in each step).
        while j >= 0 and A[i] * B[j] > m:
          j -= 1
        # All elements from B[0] to B[j] (inclusive) will satisfy A[i] * B_val <= m.
        # So, (j + 1) elements contribute.
        ans += j + 1
      return ans

    # Binary search for the absolute value of the k-th smallest product.
    # The range of possible products is from 0 to 10^10 (approx. max_int * max_int).
    l = 0
    r = 10**10 # A sufficiently large upper bound for the absolute product

    while l < r:
      m = (l + r) // 2 # Midpoint of the search range
      
      # Calculate the total number of products (positive or negative, depending on 'sign')
      # whose absolute value is less than or equal to `m`.
      # numProductNoGreaterThan(A1, B1, m) counts products from (neg * neg) or (pos * pos)
      # when sign is 1 (finding positive products) or abs(neg*pos) when sign is -1.
      # numProductNoGreaterThan(A2, B2, m) counts products from (pos * pos) or (neg * neg)
      # depending on sign.
      
      # The combination of A1, B1 and A2, B2 here depends on how the problem
      # defines the product types and how B1/B2 were swapped for negative products.
      # If sign == 1 (finding positive products):
      #   We count products from (A1 * B1) which are (-neg * -neg = pos)
      #   And products from (A2 * B2) which are (pos * pos = pos)
      # If sign == -1 (finding negative products (abs value)):
      #   We count products from (A1 * B2) which are (abs(-neg) * abs(pos)) (using swapped B1, B2)
      #   And products from (A2 * B1) which are (abs(pos) * abs(-neg)) (using swapped B1, B2)
      
      # The logic correctly counts the total number of products <= m (absolute value).
      count_le_m = numProductNoGreaterThan(A1, B1, m) + numProductNoGreaterThan(A2, B2, m)

      # If the count of products less than or equal to `m` is >= k,
      # it means `m` might be our answer, or we can find a smaller one.
      if count_le_m >= k:
        r = m
      # Otherwise, `m` is too small, and we need to look in the larger half.
      else:
        l = m + 1

    # After binary search, `l` will hold the absolute value of the k-th smallest product.
    # Apply the determined sign.
    return sign * l

def get_list_of_integers_input(prompt: str) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if not elements:
                print("List cannot be empty. Please enter at least one integer.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    nums1_val = get_list_of_integers_input("Enter numbers for nums1 (e.g., '-2 -1 0 1 2'): ")
    nums2_val = get_list_of_integers_input("Enter numbers for nums2 (e.g., '-3 -1 0 1 2'): ")
    k_val = get_integer_input("Enter the value of k (the k-th smallest product): ")

    result = sol.kthSmallestProduct(nums1_val, nums2_val, k_val)
    print(f"The {k_val}-th smallest product is: {result}")