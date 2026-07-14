class Solution:
    def canIWin(self, m, t):
        if t <= 0:
            return True
        if m * (m + 1) // 2 < t:
            return False

        dp = {}

        def dfs(mask, total):
            if mask in dp:
                return dp[mask]

            for i in range(m):
                if not (mask >> i) & 1:
                    if i + 1 >= total or not dfs(mask | (1 << i), total - i - 1):
                        dp[mask] = True
                        return True
            dp[mask] = False
            return False

        return dfs(0, t)