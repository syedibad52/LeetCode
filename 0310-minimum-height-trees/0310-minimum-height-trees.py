from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        q = deque(i for i in range(n) if deg[i] == 1)

        while n > 2:
            n -= len(q)
            for _ in range(len(q)):
                x = q.popleft()
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)

        return list(q)