import heapq
import math
from typing import List, Tuple

class Solution:
  def minTimeToReach(self, moveTime: List[List[int]]) -> int:
    return self._dijkstra(moveTime,
                          (0, 0),
                          (len(moveTime) - 1, len(moveTime[0]) - 1))

  def _dijkstra(
      self,
      moveTime: List[List[int]],
      src: Tuple[int, int],
      dst: Tuple[int, int]
  ) -> int:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(moveTime)
    n = len(moveTime[0])
    dist = [[math.inf] * n for _ in range(m)]

    dist[0][0] = 0
    minHeap = [(0, src)]  # (d, u)

    while minHeap:
      d, u = heapq.heappop(minHeap)
      if u == dst:
        return d
      i, j = u
      if d > dist[i][j]:
        continue
      for dx, dy in DIRS:
        x = i + dx
        y = j + dy
        if 0 <= x < m and 0 <= y < n:
          newDist = max(moveTime[x][y], d) + 1
          if newDist < dist[x][y]:
            dist[x][y] = newDist
            heapq.heappush(minHeap, (newDist, (x, y)))

    return -1

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    moveTime1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Minimum time to reach for {moveTime1}: {sol.minTimeToReach(moveTime1)}")

    moveTime2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(f"Minimum time to reach for {moveTime2}: {sol.minTimeToReach(moveTime2)}")

    moveTime3 = [[5]]
    print(f"Minimum time to reach for {moveTime3}: {sol.minTimeToReach(moveTime3)}")

    moveTime4 = [[5, 2], [4, 1]]
    print(f"Minimum time to reach for {moveTime4}: {sol.minTimeToReach(moveTime4)}")