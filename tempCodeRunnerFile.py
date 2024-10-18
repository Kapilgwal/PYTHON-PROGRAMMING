class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Initialize parent list
        self.rank = [0] * n  # Initialize rank list
    
    def findUParent(self, u):
        if self.parent[u] == u:  # If the node is its own parent
            return u
        else:
            # Path compression by pointing the node directly to its ultimate parent
            self.parent[u] = self.findUParent(self.parent[u])
            return self.parent[u]
    
    def unionByRank(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        
        if ulp_u == ulp_v:  # They are already in the same set
            return 
        
        # Union by rank
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [4, 5], [5, 6], [6, 7], [4, 7]]
    n = 8  # Since nodes are 1-based, the array should handle up to index 7 (n=8)
    ds = DisjointSet(n)
    
    for u, v in edges:
        ds.unionByRank(u, v)
        
        if ds.findUParent(3) == ds.findUParent(7):
            print("True")
