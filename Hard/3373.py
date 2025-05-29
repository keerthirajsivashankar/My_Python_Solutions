from typing import List, Tuple
import collections

class Solution:
  def maxTargetNodes(
      self,
      edges1: List[List[int]],
      edges2: List[List[int]],
      k: int
  ) -> List[int]:
    graph1 = self._buildGraph(edges1)
    graph2 = self._buildGraph(edges2)
    maxReachableInGraph2 = 0

    num_nodes_g2 = len(edges2) + 1 if edges2 else 1

    if k > 0:
      for i in range(num_nodes_g2):
        maxReachableInGraph2 = max(maxReachableInGraph2,
                                   self._dfs(graph2, i, -1, k - 1))

    num_nodes_g1 = len(edges1) + 1 if edges1 else 1

    return [maxReachableInGraph2 + self._dfs(graph1, i, -1, k)
            for i in range(num_nodes_g1)]

  def _dfs(self, graph: List[List[int]], u: int, prev: int, k: int) -> int:
    if k == 0:
      return 1
    res = 0
    for v in graph[u]:
      if v != prev:
        res += self._dfs(graph, v, u, k - 1)
    return 1 + res

  def _buildGraph(self, edges: List[List[int]]) -> List[List[int]]:
    num_nodes = len(edges) + 1 if edges else 1
    graph = [[] for _ in range(num_nodes)]
    for u, v in edges:
      if 0 <= u < num_nodes and 0 <= v < num_nodes:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_edges_input(graph_name: str) -> List[List[int]]:
    edges = []
    print(f"\nEnter edges for {graph_name}.")
    print("Each edge should be two space-separated node indices (e.g., '0 1').")
    print("The number of nodes in this graph will be inferred as (number of edges + 1).")
    print("Enter 'done' when you have finished entering edges.")

    while True:
        line = input(f"Edge for {graph_name} (or 'done'): ").strip()
        if line.lower() == 'done':
            break
        if not line:
            continue
        try:
            u, v = map(int, line.split())
            if u < 0 or v < 0:
                print("Node indices must be non-negative.")
                continue
            edges.append([u, v])
        except ValueError:
            print("Invalid input. Please enter two space-separated integers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    return edges

def get_k_input() -> int:
    while True:
        try:
            k_val = int(input("\nEnter the integer k (number of steps): "))
            if k_val < 0:
                print("k must be a non-negative integer.")
            else:
                return k_val
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()

    print("--- Max Target Nodes Calculation ---")
    print("This program calculates a value based on reachable nodes in two graphs.")
    print("Note: The number of nodes in each graph is determined by (number of edges + 1).")

    edges1_input = get_edges_input("Graph 1")
    edges2_input = get_edges_input("Graph 2")
    k_input = get_k_input()

    result = sol.maxTargetNodes(edges1_input, edges2_input, k_input)

    print(f"\nResulting list of max target nodes: {result}")