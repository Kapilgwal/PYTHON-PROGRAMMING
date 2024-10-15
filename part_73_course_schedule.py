def dfs(node, vis, adj, ans):
    vis[node] = 1
    
    for neighbour in adj[node]:
        if vis[neighbour] == 0:
            dfs(neighbour, vis, adj, ans) 
    ans.append(node)

def courseSchedules(edges: list[list[int]], v: int) -> list[int]:
    adj = [[] for _ in range(v)]
    
    for u, vertex in edges: 
        adj[u].append(vertex)
        
    ans = []
    vis = [0] * v
    for i in range(v):
        if vis[i] == 0:
            dfs(i, vis, adj, ans)
    
    return ans[::-1] 


def main():
    edges = [[1, 0], [2, 1], [3, 2]]
    v = 4
    ans = courseSchedules(edges, v)
    print(ans)

if __name__ == "__main__":
    main()
