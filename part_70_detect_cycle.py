from collections import deque

def dfs(node, vis, adjList, parent) -> bool:
    vis[node] = True 
    parent[node] = 1  # Mark node as part of the recursion stack
    
    for adjNode in adjList[node]:
        if not vis[adjNode]:
            if dfs(adjNode, vis, adjList, parent):
                return True 
        elif parent[adjNode]:  # If an adjacent node is already in the recursion stack, cycle is found
            return True
    
    parent[node] = 0  # Unmark node from recursion stack
    return False
    

def detectCycle(edges: list[list[int]], num_vertices: int) -> bool:
    adjList = [[] for _ in range(num_vertices + 1)]
    
    # Build adjacency list for undirected graph
    for it in edges:
        u = it[0]
        w = it[1]  # Renamed variable to avoid shadowing `v`
        adjList[u].append(w)
        adjList[w].append(u)
    
    vis = [0] * (num_vertices + 1)
    parent = [0] * (num_vertices + 1)
    
    # Loop through each node to detect cycle (handles disconnected graphs as well)
    for i in range(1, num_vertices + 1):
        if not vis[i]:
            if dfs(i, vis, adjList, parent):
                return True 
    
    return False
            

def main():
    # Example input with a cycle
    edges = [
        [1, 2], [2, 3], [3, 4], [3, 7], 
        [4, 5], [7, 5], [5, 6], 
        [8, 9], [9, 10], [10, 8], [8, 2]
    ]
    num_vertices = 10
    ans = detectCycle(edges, num_vertices)
    print(ans)

if __name__ == "__main__":
    main()
