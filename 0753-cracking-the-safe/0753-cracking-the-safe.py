class Solution:
    def crackSafe(self, n, k):
        seen = set()
        ans = []

        def dfs(node):
            for x in map(str, range(k)):
                nxt = node + x
                if nxt not in seen:
                    seen.add(nxt)
                    dfs(nxt[1:])
                    ans.append(x)

        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)