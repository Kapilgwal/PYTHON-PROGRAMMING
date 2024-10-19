class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n 
        
    def findUParent(self, node):
        if self.parent[node] == node:
            return self.parent[node]
        # Path compression
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)

        if ulp_u == ulp_v:
            return 
        
        # Union by size
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

def makeLargestIsland(grid: list[list[int]]) -> int:
    n = len(grid)
    ds = DisjointSet(n * n)
    
    # Step 1: Union all adjacent '1's
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                continue
            
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            
            for i in range(4):
                nrow = row + dr[i]
                ncol = col + dc[i]
                
                if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 1:
                    nodeNo = row * n + col 
                    adjNodeNo = nrow * n + ncol 
                    ds.unionBySize(nodeNo, adjNodeNo)
    
    # Step 2: Try flipping each '0' to '1' and calculate the new island size
    mx = 0
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                continue
            
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            
            # Collect unique components around the current '0'
            component = set()
            for i in range(4):
                nrow = row + dr[i]
                ncol = col + dc[i]
                
                if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 1:
                    component.add(ds.findUParent(nrow * n + ncol))
            
            # Calculate total size of the new island after flipping '0' to '1'
            total = 1  # We flip this '0' to '1'
            for it in component:
                total += ds.size[it]
            
            mx = max(mx, total)
    
    # Step 3: Check the largest island without flipping any '0' (if all are '1's)
    for cellNo in range(n * n):
        if grid[cellNo // n][cellNo % n] == 1:
            mx = max(mx, ds.size[ds.findUParent(cellNo)])
        
    return mx

def main():
    grid = [
        [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0],
    ]

    ans = makeLargestIsland(grid)
    print(ans)
    
if __name__ == "__main__":
    main()
