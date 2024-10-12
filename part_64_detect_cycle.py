from collections import deque

class Solution:
    def detect(self, src: int, adj: list[list[int]], vis: list[int]) -> bool:
        vis[src] = 1
        q = deque()
        q.append((src, -1))

        while q:
            node, parent = q.popleft()

            for adjacent_node in adj[node]:
                if not vis[adjacent_node]:
                    vis[adjacent_node] = 1
                    q.append((adjacent_node, node))
                elif parent != adjacent_node:
                    return True

        return False

    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.detect(i, adj, vis):
                    return True
        return False

    def detectDFS(self, src: int, adj: list[list[int]], vis: list[int], parent: int) -> bool:
        vis[src] = 1

        for adjacent_node in adj[src]:
            if not vis[adjacent_node]:
                if self.detectDFS(adjacent_node, adj, vis, src):
                    return True
            elif adjacent_node != parent:
                return True

        return False

    def isCycleDFS(self, V: int, adj: list[list[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.detectDFS(i, adj, vis, -1):
                    return True
        return False

# Example usage
if __name__ == "__main__":
    adj = [[], [2], [1, 3], [2]]
    obj = Solution()
    ans1 = obj.isCycle(4, adj)  # Check for cycle using BFS
    ans2 = obj.isCycleDFS(4, adj)  # Check for cycle using DFS
    print(ans1, ans2)  # Output the results
