from collections import deque

def floodFill(image : list[list[int]],sr : int,sc : int) -> list[list[int]]:
    n = len(image)
    m = len(image[0])
    
    vis = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([])
    q.append([sr,sc])
    vis[sr][sc] = 1
    image[sr][sc] = 2
    while q:
        node = q.popleft()
        row = node[0]
        col = node[1]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        for i in range(4):
            nrow = dr[i] + row 
            ncol = dc[i] + col 
            
            if 0 <= nrow < n and 0 <= ncol < m:
                if vis[nrow][ncol] == 0 and image[nrow][ncol] == 1:
                    image[nrow][ncol] = 2
                    q.append([nrow,ncol])
                    vis[nrow][ncol] = 1
    
    return image 

def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newCol = 2
    print(image)
    ans = floodFill(image,sr,sc)
    print(ans)
    
if __name__ == "__main__":
    main()