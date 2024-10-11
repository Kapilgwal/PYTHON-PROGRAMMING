from collections import deque

def adjList(edges,v):
    adj = [[] for _ in range(v+1)]
    
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        adj[u].append(v)
        adj[v].append(u)
    
    return adj
        

def breadthFirstSearch(edges,v):
    adj = adjList(edges,v)
    q = deque()
    q.append(1)
    ans = []
    vis = [0] * (v+1) 
    
    
    while q:
        node = q.popleft()
        
        ans.append(node)
        
        for i in adj[node]:
            if not vis[i]:
                q.append(i)
                vis[i] = True
    
    return ans
        
def dfs(adj,vis,ans,i):
    vis[i] = True
    ans.append(i)
    
    for j in adj[i]:
        if not vis[j]:
            dfs(adj,vis,ans,j)   
    
def depthFirstSearch(edges,v):
    adj = adjList(edges,v)
    vis = [0] * (v+1)
    ans = []
    for i in range(v+1):
        
        if vis[i] == 0:
            dfs(adj,vis,ans,i)
    
    
    return ans
            


def main():
    edges = [[1,3],[1,2],[3,4],[4,5],[5,6],[5,7]]
    v = 7
    bfs = breadthFirstSearch(edges,v)
    dfs = depthFirstSearch(edges,v)
    print(bfs)
    print(dfs)
    
if __name__ == "__main__":
    main()