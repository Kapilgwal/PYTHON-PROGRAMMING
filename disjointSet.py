class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def findUParent(self, node: int):
        if self.parent[node] == node:
            return node

        else:
            self.parent[node] = self.findUParent(self.parent[node])
            return self.parent[node]

    def unionByRank(self, u: int, v: int) -> None:

        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)

        if ulp_u == ulp_v:
            return

        elif self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v

        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u

        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u: int, v: int) -> None:

        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)

        if ulp_u == ulp_v:
            return

        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


if __name__ == "__main__":

    edges = [[1, 2], [2, 3], [4, 5], [5, 6], [6, 7], [3, 7]]
    n = 7
    ds = DisjointSet(n + 1)
    for u, v in edges:
        ds.unionByRank(u, v)

        if ds.findUParent(3) == ds.findUParent(7):
            print("True")
