from collections import deque

def dfs(node, vis, adj, ans):
    vis[node] = 1
    
    for adjNode in adj[node]:
        if not vis[adjNode]:
            dfs(adjNode, vis, adj, ans)
    
    ans.append(node)

def topoSortDFS(edges: list[list[int]], v: int) -> list[int]:
    adj = [[] for _ in range(v)]
    
    for edge in edges:
        adj[edge[0]].append(edge[1])

    vis = [0] * v
    ans = []
    for i in range(v):
        if not vis[i]:
            dfs(i, vis, adj, ans)
    
    return ans[::-1]

def topoSortBFS(edges: list[list[int]], v: int) -> list[int]:
    adj = [[] for _ in range(v)]
    indegree = [0] * v
    
    for u, vtx in edges:
        adj[u].append(vtx)
        indegree[vtx] += 1

    queue = deque([i for i in range(v) if indegree[i] == 0])
    
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) == v:
        return topo_order
    else:
        return []

def main():
    edges = [[5, 0], [4, 0], [2, 3], [3, 1], [4, 1], [5, 2]]
    v = 6
    ans1 = topoSortDFS(edges, v)
    ans2 = topoSortBFS(edges, v)
    print("Topological Sort (DFS):", ans1)
    print("Topological Sort (BFS):", ans2)

if __name__ == "__main__":
    main()
