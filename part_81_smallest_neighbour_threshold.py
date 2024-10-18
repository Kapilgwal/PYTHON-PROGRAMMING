from collections import deque

def smallestNeighbourThreshold(edges,n,maxDis):
    dist = [[1e9 for _ in range(n)] for _ in range(n)]
    
    for u,v,w in edges:
        dist[u][v] = w    
        dist[v][u] = w    
        
    for i in range(n):
        dist[i][i] = 0
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                if dist[i][k] == 1e9 or dist[k][j] == 1e9:
                    continue
                
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    
    cntCity = n
    cityNo = -1
    
    for city in range(n):
        cnt = 0
        for adjcity in range(n):
            if dist[city][adjcity] <= maxDis:
                cnt += 1
        
        if cnt <= cntCity:
            cntCity = cnt
            cityNo = city 
    
    return cityNo
        
        

def main():
    N=4
    M=4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold = 4
    ans = smallestNeighbourThreshold(edges,N,distanceThreshold)
    print(ans)
    
if __name__ == "__main__":
    main()