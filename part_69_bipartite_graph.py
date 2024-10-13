from collections import deque

def bipartiteGraph(edges: list[list[int]], v: int) -> bool:
    adjList = [[] for _ in range(v + 1)]

    for i in edges:
        u = i[0]
        v = i[1]

        adjList[u].append(v)
        adjList[v].append(u)

    color = [-1] * (v + 1)

    for start in range(1, v + 1):
        if color[start] == -1:
            q = deque([[start, 0]])
            color[start] = 0

            while q:
                node, col = q.popleft()

                for adjNode in adjList[node]:

                    if color[adjNode] == -1:
                        color[adjNode] = not col
                        q.append([adjNode, not col])

                    if color[node] == color[adjNode]:
                        return False

    return True


def main():
    edges = [
    [1, 2], [1, 3], 
    [2, 4], [3, 5], 
    [4, 6], [5, 6]]
    v = 6
    ans = bipartiteGraph(edges, 10)
    print(ans)


if __name__ == "__main__":
    main()
