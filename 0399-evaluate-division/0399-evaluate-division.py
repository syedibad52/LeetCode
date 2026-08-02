from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(cur, target, visited):
            if cur == target:
                return 1.0

            visited.add(cur)

            for nei, val in graph[cur]:
                if nei not in visited:
                    ans = dfs(nei, target, visited)
                    if ans != -1:
                        return val * ans

            return -1

        ans = []

        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))

        return ans