import heapq

def shortestPath(grid : list[list[int]],src : list[int],dest : list[int]) -> int:
    pq = []
    heapq.heappush(pq,(grid[src[0][0]][src[0][1]], src))
    
    while pq:
        dist,node = heapq.heappop()
        
        if node == dest:
            return dist 
        
        for adjNode in adj[node]
    

def main():
    grid = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1]]
    source = [0, 1]
    destination = [2, 2]
    ans = shortestPath(grid,source,destination)
    print(ans)
    
if __name__ == "__main__":
    main()