class UnionFind:
    def __init__(self, n: int):
        self.id = list(range(n))
        self.rank = [0] * n
        self.node_count = [1] * n
        self.edge_count = [0] * n

    def union_by_rank(self, u: int, v: int) -> None:
        i = self.find(u)
        j = self.find(v)
        self.edge_count[i] += 1
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
            self.edge_count[j] += self.edge_count[i]
            self.node_count[j] += self.node_count[i]
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
            self.edge_count[i] += self.edge_count[j]
            self.node_count[i] += self.node_count[j]
        else:
            self.id[i] = j
            self.edge_count[j] += self.edge_count[i]
            self.node_count[j] += self.node_count[i]
            self.rank[j] += 1

    def find(self, u: int) -> int:
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

    def is_complete(self, u):
        return self.node_count[u] * (self.node_count[u] - 1) // 2 == self.edge_count[u]


def count_complete_components(n: int, edges: list[list[int]]) -> int:
    ans = 0
    uf = UnionFind(n)
    parents = set()

    for u, v in edges:
        uf.union_by_rank(u, v)

    for i in range(n):
        parent = uf.find(i)
        if parent not in parents and uf.is_complete(parent):
            ans += 1
            parents.add(parent)

    return ans

if __name__ == "__main__":
    n1 = 6
    edges1 = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    result1 = count_complete_components(n1, edges1)
    print(f"Complete components for {edges1}: {result1}")

    n2 = 6
    edges2 = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5], [4, 5]]
    result2 = count_complete_components(n2, edges2)
    print(f"Complete components for {edges2}: {result2}")

    n3 = 6
    edges3 = [[0,1],[2,3],[4,5]]
    result3 = count_complete_components(n3,edges3)
    print(f"Complete components for {edges3}: {result3}")

    n4 = 1
    edges4 = []
    result4 = count_complete_components(n4,edges4)
    print(f"Complete components for {edges4}: {result4}")

    n5 = 5
    edges5 = [[0,1],[1,2],[2,3],[3,0]]
    result5 = count_complete_components(n5,edges5)
    print(f"Complete components for {edges5}: {result5}")