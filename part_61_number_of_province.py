def dfs(node,adjList,vis):
    
    vis[node] = 1
    
    for i in adjList[node]:
        
        if vis[i] == 0:
            dfs(i,adjList,vis)


def noOfProvince(adj : list[list[int]]) -> int:
    v = len(adj)
    
    adjList = [[]for _ in range(v+1)]
    
    for i in range(v):
        for j in range(v):
            if adj[i][j] == 1 and i != j:
                adjList[i].append(j)
                adjList[j].append(i)
    
    cnt = 0
    vis = [0] * (v+1)
    
    for i in range(v):
        
        if vis[i] == 0:
            cnt += 1
            dfs(i,adjList,vis)       
    
    return cnt 
    

def main():
    adj = [[1, 0, 1],[0, 1, 0],[1, 0, 1]]
    ans = noOfProvince(adj)
    print(ans)
    
if __name__ == "__main__":
    main()