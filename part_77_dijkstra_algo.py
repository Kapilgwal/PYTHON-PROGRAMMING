import heapq

def dijkstraAlgo(adj, V: int, src: int) -> list[int]:
    pq = []
    
    dist = [float('inf')] * V
    dist[src] = 0
    
    heapq.heappush(pq, (0, src))
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > dist[node]:
            continue
        
        for adjNode, weight in adj[node]:
            new_dist = current_dist + weight
            
            if new_dist < dist[adjNode]:
                dist[adjNode] = new_dist
                heapq.heappush(pq, (new_dist, adjNode))
    
    return dist

def main():
    V = 3
    adj = [[(1, 1), (2, 6)], [(2, 3), (0, 1)], [(1, 3), (0, 6)]]
    src = 2  # Source node
    ans = dijkstraAlgo(adj, V, src)
    print("Shortest distances from node", src, "to all other nodes:", ans)

if __name__ == "__main__":
    main()
