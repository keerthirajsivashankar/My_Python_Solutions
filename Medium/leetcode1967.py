import heapq
import math

def count_paths(n: int, roads: list[list[int]]) -> int:
    """
    Counts the number of shortest paths from source to destination in a graph.

    Args:
        n: The number of nodes in the graph.
        roads: A list of edges, where each edge is [u, v, w] (u, v are nodes, w is weight).

    Returns:
        The number of shortest paths from source to destination.
    """
    graph = [[] for _ in range(n)]

    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return _dijkstra(graph, 0, n - 1)

def _dijkstra(graph: list[list[tuple[int, int]]], src: int, dst: int) -> int:
    """
    Dijkstra's algorithm to find the number of shortest paths.

    Args:
        graph: The graph represented as an adjacency list.
        src: The source node.
        dst: The destination node.

    Returns:
        The number of shortest paths from source to destination.
    """
    MOD = 10**9 + 7
    ways = [0] * len(graph)
    dist = [math.inf] * len(graph)

    ways[src] = 1
    dist[src] = 0
    min_heap = [(dist[src], src)]

    while min_heap:
        d, u = heapq.heappop(min_heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                ways[v] = ways[u]
                heapq.heappush(min_heap, (dist[v], v))
            elif d + w == dist[v]:
                ways[v] += ways[u]
                ways[v] %= MOD

    return ways[dst]

if __name__ == "__main__":
    n1 = 7
    roads1 = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [6, 3, 3], [3, 2, 2], [6, 5, 1], [5, 4, 2], [4, 3, 1]]
    result1 = count_paths(n1, roads1)
    print(f"Paths for {roads1}: {result1}")

    n2 = 2
    roads2 = [[1, 0, 10]]
    result2 = count_paths(n2, roads2)
    print(f"Paths for {roads2}: {result2}")

    n3 = 3
    roads3 = [[0,1,1],[1,2,1],[0,2,2]]
    result3 = count_paths(n3, roads3)
    print(f"Paths for {roads3}: {result3}")

    n4 = 5
    roads4 = [[0,1,1],[1,2,1],[2,3,1],[3,4,1]]
    result4 = count_paths(n4, roads4)
    print(f"Paths for {roads4}: {result4}")

    n5 = 5
    roads5 = [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[0,4,4]]
    result5 = count_paths(n5, roads5)
    print(f"Paths for {roads5}: {result5}")