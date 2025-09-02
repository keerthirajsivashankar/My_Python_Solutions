from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Counts the number of pairs of points (p1, p2) such that p2 is in the
        bottom-right quadrant relative to p1.
        A pair is valid if p1.x <= p2.x and p1.y >= p2.y.
        """
        # Sort points first by x-coordinate in ascending order.
        # If x-coordinates are equal, sort by y-coordinate in descending order.
        points.sort(key=lambda p: (p[0], -p[1]))

        # Initialize the counter for valid pairs.
        count = 0

        # Iterate through each point as the potential top-left point of the pair.
        for i in range(len(points)):
            x1, y1 = points[i]

            # Iterate through all subsequent points as the potential bottom-right point.
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                
                # Because the list is sorted by x, we know that x2 >= x1.
                # We only need to check the y-coordinate condition.
                # A pair is valid if p2 is in the bottom-right quadrant relative to p1,
                # which means p2.y <= p1.y.
                if y2 <= y1:
                    count += 1
        
        return count

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    points1 = [[1, 1], [2, 2], [3, 3]]
    result1 = sol.numberOfPairs(points1)
    print(f"Points: {points1}")
    print(f"Number of pairs: {result1}")
    print("-" * 20)

    # Test case 2
    points2 = [[6,2],[4,4],[2,6],[1,1]]
    result2 = sol.numberOfPairs(points2)
    print(f"Points: {points2}")
    print(f"Number of pairs: {result2}")
    print("-" * 20)
    
    # Test case 3
    points3 = [[2, 2], [3, 1], [1, 3]]
    result3 = sol.numberOfPairs(points3)
    print(f"Points: {points3}")
    print(f"Number of pairs: {result3}")
