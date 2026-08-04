class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            ans = 1

            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(ni, nj))

            dp[i][j] = ans
            return ans

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res