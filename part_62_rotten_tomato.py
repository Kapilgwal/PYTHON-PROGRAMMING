from collections import deque 

def minTime(grid : list[list[int]]) -> int:
    
    q = deque([])
    n = len(grid)
    m = len(grid[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            
            if grid[i][j] == 2:
                q.append([i,j,0])
                vis[i][j] = 1
                
    
    time = 0
    while q:
        node = q.popleft()
        
        row = node[0]
        col = node[1]
        currTime = node[2]
        time = max(time,currTime)
        
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        for i in range(4):
            nrow = dr[i] + row 
            ncol = dc[i] + col
            
            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < n:
                if vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    q.append([nrow,ncol,currTime+1])
    
    
    for i in range(n):
        for j in range(m):
            
            if grid[i][j] == 1:
                return -1 
    
    return time
            
            
                

def main():
    grid = [ [2,1,1] , [0,1,1] , [1,0,1] ]
    ans = minTime(grid)
    print(ans)
    
if __name__ == "__main__":
    main()