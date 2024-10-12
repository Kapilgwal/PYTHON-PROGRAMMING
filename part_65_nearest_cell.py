from collections import deque

def nearestCell(matrix : list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    
    vis = [[0 for i in range(m)] for i in range(n)]
    dis = [[-1 for i in range(m)] for i in range(n)]
    q = deque([])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                q.append([i,j,0])
                vis[i][j] = 1 
            else:
                vis[i][j] = 0
    
    while q:
        front = q.popleft()
        row = front[0]
        col = front[1]
        dist = front[2]
        
        dis[row][col] = dist
        
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            
            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0:
                vis[nrow][ncol] = 1
                q.append([nrow,ncol,dist + 1])
    
    return dis
                
    
def main():
    matrix = [[1,0,1],[1,1,0],[1,0,0]]
    ans = nearestCell(matrix)
    print(ans)
    
if __name__ == "__main__":
    main()