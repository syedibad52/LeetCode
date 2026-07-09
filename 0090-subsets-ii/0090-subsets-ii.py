class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []

        def dfs(i, path):
            ans.append(path)

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(j + 1, path + [nums[j]])

        dfs(0, [])
        return ans