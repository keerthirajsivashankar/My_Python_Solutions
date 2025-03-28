from dataclasses import dataclass
import heapq

@dataclass(frozen=True)
class IndexedQuery:
    query_index: int
    query: int

    def __iter__(self):
        yield self.query_index
        yield self.query

def max_points(grid: list[list[int]], queries: list[int]) -> list[int]:
    """
    Calculates the number of points reachable in a grid for each query.

    Args:
        grid: A 2D list representing the grid.
        queries: A list of integer queries.

    Returns:
        A list of counts of reachable points for each query.
    """
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(grid)
    n = len(grid[0])
    ans = [0] * len(queries)
    min_heap = [(grid[0][0], 0, 0)]  # (grid[i][j], i, j)
    seen = {(0, 0)}
    accumulate = 0

    sorted_queries = sorted([IndexedQuery(i, query) for i, query in enumerate(queries)], key=lambda x: x.query)

    for query_index, query in sorted_queries:
        while min_heap:
            val, i, j = heapq.heappop(min_heap)
            if val >= query:
                heapq.heappush(min_heap, (val, i, j))
                break
            accumulate += 1
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if (x, y) in seen:
                    continue
                heapq.heappush(min_heap, (grid[x][y], x, y))
                seen.add((x, y))
        ans[query_index] = accumulate

    return ans

if __name__ == "__main__":
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    queries1 = [2, 5, 8]
    result1 = max_points(grid1, queries1)
    print(f"Max points for {grid1}, {queries1}: {result1}")

    grid2 = [[1, 2, 3], [4, 5, 6]]
    queries2 = [2, 5]
    result2 = max_points(grid2, queries2)
    print(f"Max points for {grid2}, {queries2}: {result2}")

    grid3 = [[10, 11, 12], [13, 14, 15]]
    queries3 = [10, 12, 14, 16]
    result3 = max_points(grid3, queries3)
    print(f"Max points for {grid3}, {queries3}: {result3}")

    grid4 = [[1]]
    queries4 = [1]
    result4 = max_points(grid4, queries4)
    print(f"Max points for {grid4}, {queries4}: {result4}")

    grid5 = [[1,2],[3,4]]
    queries5 = [3]
    result5 = max_points(grid5, queries5)
    print(f"Max points for {grid5}, {queries5}: {result5}")