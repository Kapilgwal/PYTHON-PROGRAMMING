import heapq

def shortestPath(heights) -> int:
    pq = []
    n = len(heights)
    m = len(heights[0])
    
  
    dist = [[1e9 for _ in range(m)] for _ in range(n)]
    
    x, y = 0, 0  
    dist[0][0] = 0  
    heapq.heappush(pq, (0, x, y))
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)  
        if (row, col) == (n - 1, m - 1):
            return current_dist

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
    
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            
        
            if 0 <= nrow < n and 0 <= ncol < m:
                new_dist = max(current_dist, abs(heights[nrow][ncol] - heights[row][col]))
                
                if new_dist < dist[nrow][ncol]:
                    dist[nrow][ncol] = new_dist
                    heapq.heappush(pq, (new_dist, nrow, ncol))
    
    return -1

def main():
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    ans = shortestPath(heights)
    print(ans)

if __name__ == "__main__":
    main()
