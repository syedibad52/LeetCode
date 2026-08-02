from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        g = defaultdict(list)

        for (a, b), v in zip(equations, values):
            g[a].append((b, v))
            g[b].append((a, 1 / v))

        def dfs(x, y, val, vis):
            if x == y:
                return val
            vis.add(x)
            for nxt, w in g[x]:
                if nxt not in vis:
                    ans = dfs(nxt, y, val * w, vis)
                    if ans != -1:
                        return ans
            return -1

        res = []
        for a, b in queries:
            if a not in g or b not in g:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, 1, set()))
        return res