class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(i, total, path):
            if total == target:
                ans.append(path)
                return
            if total > target or i == len(candidates):
                return

            dfs(i, total + candidates[i], path + [candidates[i]])
            dfs(i + 1 , total, path)

        dfs(0, 0, [])
        return ans