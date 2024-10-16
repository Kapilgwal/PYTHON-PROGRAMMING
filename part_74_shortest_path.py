from collections import deque

def shortestPath(edges: list[list[int]], n: int, m: int, src: int) -> list[int]:
    # Initialize adjacency list for the graph
    adj = [[] for _ in range(n)]
    
    # Populate the adjacency list with given edges
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize distance array with infinity
    dist = [1e9] * n
    
    # Using deque for BFS and starting from the source node
    q = deque([src])
    dist[src] = 0  # Distance to source is 0
    
    while q:
        node = q.popleft()
        
        # Check the adjacent nodes of the current node
        for adjNode in adj[node]:
            if dist[node] + 1 < dist[adjNode]:
                dist[adjNode] = 1 + dist[node]  # Update distance to the adjacent node
                q.append(adjNode)
    
    # Prepare the answer list
    ans = [-1] * n
    for i in range(n):
        if dist[i] != 1e9:
            ans[i] = dist[i] 
    
    return ans

def main():
    # Graph edges (node pairs)
    edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [5, 6], [2, 6], [6, 7], [6, 8], [7, 8]]
    n = 9  # Number of nodes
    m = 10  # Number of edges
    src = 0  # Source node
    
    ans = shortestPath(edges, n, m, src)
    print(ans)

if __name__ == "__main__":
    main()
