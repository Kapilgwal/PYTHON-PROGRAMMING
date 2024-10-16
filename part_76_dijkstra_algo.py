def dijkstraAlgo(adj, V: int, src: int) -> list[int]:
    st = set()
    dist = [float("inf")] * V
    st.add((0, src))
    
    dist[src] = 0
    
    while st:
        dis, node = min(st)
        st.remove((dis, node))
        
        for adjNode, edW in adj[node]:
            if dis + edW < dist[adjNode]:
                if dist[adjNode] != float('inf'):
                    st.discard((dist[adjNode], adjNode))
                
               
                dist[adjNode] = dis + edW
                st.add((dist[adjNode], adjNode))
    
    return dist

def main():
    V = 3
    adj = [[(1, 1), (2, 6)],[(2, 3), (0, 1)],[(1, 3), (0, 6)]]
    src = 2 
    ans = dijkstraAlgo(adj, V, src)
    print(ans)

if __name__ == "__main__":
    main()
