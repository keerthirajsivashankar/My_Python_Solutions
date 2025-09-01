import heapq

class Solution:
    def maxAverageRatio(
        self,
        classes: list[list[int]],
        extraStudents: int,
    ) -> float:
        """
        Maximizes the average pass ratio by strategically adding extra students.
        
        This is a greedy algorithm where we always give an extra student
        to the class that will provide the biggest increase to the average ratio.
        A max-heap is used to efficiently find the best class at each step.
        """

        def extraPassRatio(pas: int, total: int) -> float:
            """
            Calculates the potential increase in pass ratio if a student joins.
            This is the metric used to prioritize which class to add a student to.
            """
            return (pas + 1) / (total + 1) - pas / total

        # Initialize a max-heap to store the classes.
        # Python's heapq is a min-heap, so we store the negative of the
        # extra pass ratio to simulate a max-heap.
        maxHeap = [
            (-extraPassRatio(pas, total), pas, total)
            for pas, total in classes
        ]
        heapq.heapify(maxHeap)

        # Distribute the extra students one by one, always picking the
        # class with the highest potential gain from the heap.
        for _ in range(extraStudents):
            # Pop the class with the highest pass ratio increase.
            _, pas, total = heapq.heappop(maxHeap)
            
            # Add one student to the class (one pass, one total).
            pas += 1
            total += 1
            
            # Push the updated class back onto the heap with its new potential.
            heapq.heappush(
                maxHeap, (-extraPassRatio(pas, total), pas, total)
            )

        # Calculate the final average ratio of all classes.
        final_sum_of_ratios = sum(pas / total for _, pas, total in maxHeap)
        return final_sum_of_ratios / len(maxHeap)

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    classes1 = [[1, 2], [3, 5], [2, 2]]
    extraStudents1 = 2
    result1 = sol.maxAverageRatio(classes1, extraStudents1)
    print(f"Example 1: Classes = {classes1}, Extra Students = {extraStudents1}")
    print(f"Max Average Ratio: {result1:.5f}") # Expected output: 0.78333

    print("-" * 20)

    # Example 2
    classes2 = [[2, 4], [3, 9], [4, 7]]
    extraStudents2 = 3
    result2 = sol.maxAverageRatio(classes2, extraStudents2)
    print(f"Example 2: Classes = {classes2}, Extra Students = {extraStudents2}")
    print(f"Max Average Ratio: {result2:.5f}") # Expected output: 0.58431
