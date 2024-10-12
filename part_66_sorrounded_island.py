from collections import deque

def sorroundedIsland(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    vis = [[0 for i in range(m)] for j in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if i==0 or j==0 or i==n-1 or j==n-1:
                if vis[i][j] == 0 and matrix[i][j] == 0:
                    q.append([i,j])
                    vis[i][j] = 1
    
    while q:
        front = q.popleft()
        row = front[0]
        col = front[1]
        
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            
            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and matrix[nrow][ncol] == 0:
                q.append([nrow,ncol])
                vis[nrow][ncol] = 1
    
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and matrix[i][j] == 0:
                matrix[i][j] = 1
        
    return matrix     
                
                

def main():
    matrix = [[1,1,1,1],[1,0,1,1],[1,0,0,1],[1,0,1,1],[1,1,0,0]]
    ans = sorroundedIsland(matrix)
    print(ans) 

if __name__ == "__main__":
    main()