from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(x, y, vis):
            if x == y:
                return 1.0
            vis.add(x)

            for nxt, val in graph[x]:
                if nxt not in vis:
                    ans = dfs(nxt, y, vis)
                    if ans != -1:
                        return val * ans
            return -1

        res = []

        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))

        return res