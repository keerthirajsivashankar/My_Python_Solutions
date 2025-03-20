class UnionFind:
    def __init__(self, n: int):
        self.id = list(range(n))
        self.rank = [0] * n
        self.weight = [(1 << 17) - 1] * n

    def union_by_rank(self, u: int, v: int, w: int) -> None:
        i = self._find(u)
        j = self._find(v)
        new_weight = self.weight[i] & self.weight[j] & w
        self.weight[i] = new_weight
        self.weight[j] = new_weight
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j
            self.rank[j] += 1

    def get_min_cost(self, u: int, v: int) -> int:
        if u == v:
            return 0
        i = self._find(u)
        j = self._find(v)
        return self.weight[i] if i == j else -1

    def _find(self, u: int) -> int:
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])
        return self.id[u]


def minimum_cost(n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
    uf = UnionFind(n)

    for u, v, w in edges:
        uf.union_by_rank(u, v, w)

    return [uf.get_min_cost(u, v) for u, v in query]

if __name__ == "__main__":
    n1 = 4
    edges1 = [[0, 1, 3], [1, 2, 1], [2, 3, 2]]
    query1 = [[0, 2], [1, 3], [0, 3]]
    result1 = minimum_cost(n1, edges1, query1)
    print(f"Minimum costs for query {query1}: {result1}")

    n2 = 5
    edges2 = [[0, 1, 5], [1, 2, 2], [2, 3, 4], [3, 4, 1]]
    query2 = [[0, 4], [1, 3]]
    result2 = minimum_cost(n2, edges2, query2)
    print(f"Minimum costs for query {query2}: {result2}")

    n3 = 2
    edges3 = [[0,1,10]]
    query3 = [[0,1]]
    result3 = minimum_cost(n3,edges3,query3)
    print(f"Minimum costs for query {query3}: {result3}")

    n4 = 3
    edges4 = [[0,1,10],[1,2,5]]
    query4 = [[0,2]]
    result4 = minimum_cost(n4,edges4,query4)
    print(f"Minimum costs for query {query4}: {result4}")

    n5 = 5
    edges5 = [[0,1,10],[1,2,5],[2,3,2],[3,4,1]]
    query5 = [[0,4],[0,3]]
    result5 = minimum_cost(n5,edges5,query5)
    print(f"Minimum costs for query {query5}: {result5}")