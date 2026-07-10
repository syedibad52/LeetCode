class Solution:
    def findShortestSubArray(self, nums):
        d = {}

        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [1, i, i]   # count, first, last
            else:
                d[x][0] += 1
                d[x][2] = i
        degree = max(v[0] for v in d.values())
        ans = len(nums)

        for c, f, l in d.values():
            if c == degree:
                ans = min(ans, l - f + 1)

        return ans