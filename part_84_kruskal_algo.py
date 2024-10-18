class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
            
    def findUParent(self, u):
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.findUParent(self.parent[u])
            return self.parent[u]
        
    def unionByRank(self, u: int, v: int):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        
        if ulp_u == ulp_v:
            return 
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1   
                 
    def unionBySize(self, u: int, v: int):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        
        if ulp_u == ulp_v:
            return 
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
def kruskalsAlgorithm(edges: list[list[int]], n: int):
    
    ds = DisjointSet(n+1)
    edges_list = []
    
    for edge in edges:
        u = edge[0]
        v = edge[1]
        wt = edge[2]
        edges_list.append([wt, u, v])
    
    edges_list.sort()
    mstWt = 0
    
    for it in edges_list:
        wt = it[0]
        u = it[1]
        v = it[2]
        
        if ds.findUParent(u) != ds.findUParent(v):
            mstWt += wt
            ds.unionBySize(u, v)
        
    return mstWt
    

if __name__ == "__main__": 
    V = 5
    edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]
    ans = kruskalsAlgorithm(edges, V)
    print(ans)
