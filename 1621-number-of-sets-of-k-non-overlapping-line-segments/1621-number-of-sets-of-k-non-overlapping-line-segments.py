class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        r = 2 * k
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n + k - r - 1 + i) // i

        return ans % MOD