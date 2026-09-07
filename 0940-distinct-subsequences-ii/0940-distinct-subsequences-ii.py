class Solution:
    def distinctSubseqII(self, s):
        mod = 10**9 + 7
        dp = [0] * 26
        total = 0

        for c in s:
            x = ord(c) - 97
            new = (total + 1) % mod
            total = (total + new - dp[x]) % mod
            dp[x] = new

        return total