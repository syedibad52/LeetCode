from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(n) if indegree[i] == 0)

        while q:
            x = q.popleft()
            n -= 1
            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    q.append(y)

        return n == 0