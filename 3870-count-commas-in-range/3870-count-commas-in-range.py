class Solution:
    def countCommas(self, n):
        ans = 0
        for x in range(1000, n + 1):
            ans += len(str(x)) // 4
        return ans