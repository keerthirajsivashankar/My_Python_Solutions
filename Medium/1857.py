import collections
from typing import List

class Solution:
  def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    ans = 0
    processed = 0
    graph = [[] for _ in range(n)]
    inDegrees = [0] * n
    q = collections.deque()
    count = [[0] * 26 for _ in range(n)]

    # Build the graph.
    for u, v in edges:
      graph[u].append(v)
      inDegrees[v] += 1

    # Initialize queue with nodes having an in-degree of 0 (start of topological sort).
    for i, degree in enumerate(inDegrees):
      if degree == 0:
        q.append(i)

    # Perform topological sort and calculate max path value.
    while q:
      u = q.popleft()
      processed += 1
      
      # Increment the count of the current node's color.
      # This is the count of this specific color on the path ending at 'u'.
      count[u][ord(colors[u]) - ord('a')] += 1
      
      # Update the overall maximum path value found so far.
      ans = max(ans, count[u][ord(colors[u]) - ord('a')])
      
      # Propagate counts to neighbors.
      for v in graph[u]:
        # For each color, the count at neighbor 'v' is the maximum of its current count
        # and the count from the path ending at 'u'.
        for i in range(26):
          count[v][i] = max(count[v][i], count[u][i])
        
        # Decrement in-degree of neighbor 'v'.
        inDegrees[v] -= 1
        
        # If in-degree becomes 0, add to queue for processing.
        if inDegrees[v] == 0:
          q.append(v)

    # If all nodes were processed, a valid topological sort was possible (no cycle).
    # Otherwise, there's a cycle, and no valid path exists as per problem constraints.
    return ans if processed == n else -1

def get_colors_input() -> str:
    while True:
        colors_str = input("Enter the colors string (e.g., 'abacaba'): ")
        if colors_str.isalpha() and colors_str.islower():
            return colors_str
        else:
            print("Invalid input. Please enter a string of lowercase English letters only.")

def get_edges_input(num_nodes: int) -> List[List[int]]:
    edges = []
    print(f"Enter edges as pairs of node indices (u,v) separated by a comma (e.g., '0,1').")
    print(f"Enter 'done' when finished. Nodes are 0 to {num_nodes - 1}.")
    
    while True:
        edge_str = input("Edge: ")
        if edge_str.lower() == 'done':
            break
        try:
            u_str, v_str = edge_str.split(',')
            u = int(u_str.strip())
            v = int(v_str.strip())
            if not (0 <= u < num_nodes and 0 <= v < num_nodes):
                print(f"Invalid node indices. Must be between 0 and {num_nodes - 1}.")
                continue
            edges.append([u, v])
        except ValueError:
            print("Invalid format. Please enter two integers separated by a comma (e.g., '0,1').")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    return edges

if __name__ == "__main__":
    sol = Solution()

    print("--- Largest Path Value in a Directed Acyclic Graph (DAG) ---")
    
    colors_input = get_colors_input()
    num_nodes = len(colors_input)
    
    edges_input = get_edges_input(num_nodes)
    
    if num_nodes == 0:
        print("No nodes in the graph. Largest path value: 0")
    else:
        result = sol.largestPathValue(colors_input, edges_input)
        print(f"\nThe largest path value is: {result}")