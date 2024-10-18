from collections import deque
import heapq  # Using heapq to simulate a priority queue

class Solution:
    
    def spanningTree(self, edges: list[list[int]], n: int) -> int:
        # Create adjacency list
        adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # To store the minimum distance to each node and the total weight of the MST
        dist = [1e9] * n
        visited = [False] * n  # Track nodes included in MST
        minHeap = [(0, 0)]  # Priority queue (min heap) (distance, node)
        dist[0] = 0
        
        total_weight = 0  # This will store the weight of the MST
        
        while minHeap:
            currDist, node = heapq.heappop(minHeap)
            
            if visited[node]:
                continue
                
            visited[node] = True
            total_weight += currDist  # Add the edge's weight to the total MST weight
            
            for adjNode, weight in adj[node]:
                if not visited[adjNode] and weight < dist[adjNode]:
                    dist[adjNode] = weight
                    heapq.heappush(minHeap, (weight, adjNode))
        
        return total_weight
        
if __name__ == "__main__":
    edges = [[0,1,2],[0,3,6],[1,4,5],[1,2,3]]
    vertices = 5
    s = Solution()
    ans = s.spanningTree(edges, vertices)
    print(ans)
