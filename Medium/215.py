import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the Kth largest element in an unsorted array using a min-heap.

        The approach maintains a min-heap of size K.
        When iterating through the numbers:
        1. If the heap size is less than K, add the number.
        2. If the heap size is K and the current number is greater than the smallest element
           in the heap (heap[0]), then remove the smallest element and add the current number.
           This ensures the heap always contains the K largest elements seen so far,
           with the smallest of these K elements at the top.

        Args:
            nums: The list of integers.
            k: The Kth largest element to find.

        Returns:
            The Kth largest element.
        """
        heap = []  # This will be a min-heap

        for num in nums:
            # Always push the number onto the heap
            heapq.heappush(heap, num)
            
            # If the heap size exceeds k, remove the smallest element
            # This ensures the heap always contains at most k elements,
            # and those k elements are the largest ones encountered so far.
            if len(heap) > k:
                heapq.heappop(heap)
        
        # After iterating through all numbers, the smallest element in the heap
        # (heap[0]) will be the Kth largest element overall.
        return heap[0]

# Example Usage:
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    # Expected: The 2nd largest is 5 (elements are 1,2,3,4,5,6)
    print(f"Nums: {nums1}, K: {k1} -> Kth largest: {sol.findKthLargest(nums1, k1)}") # Output: 5

    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    # Expected: The 4th largest is 4 (elements are 1,2,2,3,3,4,5,5,6)
    print(f"Nums: {nums2}, K: {k2} -> Kth largest: {sol.findKthLargest(nums2, k2)}") # Output: 4

    # Test case 3 (single element)
    nums3 = [7]
    k3 = 1
    print(f"Nums: {nums3}, K: {k3} -> Kth largest: {sol.findKthLargest(nums3, k3)}") # Output: 7

    # Test case 4 (negative numbers)
    nums4 = [-1, -5, -2, -8, -3]
    k4 = 3
    # Expected: -3 (-8,-5,-3,-2,-1)
    print(f"Nums: {nums4}, K: {k4} -> Kth largest: {sol.findKthLargest(nums4, k4)}") # Output: -3