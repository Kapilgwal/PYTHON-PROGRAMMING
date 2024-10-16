def topoSort(node, adj, vis, st):
    vis[node] = 1
    
    for v, wt in adj[node]:
        if not vis[v]:
            topoSort(v, adj, vis, st)
    
    st.append(node)

def shortestPath(edges: list[list[int]], n: int, m: int) -> list[int]:
    adj = [[] for _ in range(n)]
    
    for u, v, w in edges:
        adj[u].append((v, w))
        
    vis = [0] * n 
    st = []
    
    for i in range(n):
        if vis[i] == 0:
            topoSort(i, adj, vis, st)
    
    dist = [float('inf')] * n
    dist[0] = 0
   
    while st:
        node = st.pop()
        
        if dist[node] != float('inf'):
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = wt + dist[node]
    
    ans = [-1 if d == float('inf') else d for d in dist]
    
    return ans

def main():
    edges = [[0, 1, 2], [0, 4, 1], [1, 2, 3], [4, 5, 4], [4, 2, 2], [2, 3, 6], [5, 3, 1]]
    n = 6
    m = 7
    
    ans = shortestPath(edges, n, m)
    print(ans)

if __name__ == "__main__":
    main()
