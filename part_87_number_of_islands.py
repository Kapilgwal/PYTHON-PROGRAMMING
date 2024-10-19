class DisjointSet:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n  # Initialize size as an instance variable
    
    def findUParent(self, node: int):
        if self.parent[node] == node:
            return node 
        # Path compression
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        
        if ulp_u == ulp_v:
            return 
        
        # Union by size: attach smaller tree under larger one
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

def numberOfIslands(n: int, m: int, k: int, arr: list[list[int]]) -> list[int]:
    graph = [[0 for _ in range(m)] for _ in range(n)]
    ds = DisjointSet(n * m)
    ans = []
    cnt = 0
    
    # Directions for up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    for u, v in arr:
        if graph[u][v] == 1:
            ans.append(cnt)
            continue
        
        # Mark the current cell as an island
        graph[u][v] = 1
        cnt += 1
        
        # Explore the 4 neighboring directions
        for i in range(4):
            nrow = u + dr[i]
            ncol = v + dc[i]
            
            if 0 <= nrow < n and 0 <= ncol < m:
                if graph[nrow][ncol] == 1:
                    nodeNo = u * m + v
                    adjNodeNo = nrow * m + ncol
                    
                    # If they belong to different components, merge them
                    if ds.findUParent(nodeNo) != ds.findUParent(adjNodeNo):
                        ds.unionBySize(nodeNo, adjNodeNo)
                        cnt -= 1  # Since two islands are merged, decrease the count
        
        ans.append(cnt)
    
    return ans

def main():
    n = 4
    m = 5
    k = 12
    A = [
        [0, 0],
        [0, 0],
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 3],
        [1, 3],
        [0, 4],
        [3, 2],
        [2, 2],
        [1, 2],
        [0, 2],
    ]
    ans = numberOfIslands(n, m, k, A)
    print(ans)

if __name__ == "__main__":
    main()
