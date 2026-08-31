class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        idx = [0] * len(primes)

        for i in range(1, n):
            ugly[i] = min(primes[j] * ugly[idx[j]]
                          for j in range(len(primes)))

            for j in range(len(primes)):
                if primes[j] * ugly[idx[j]] == ugly[i]:
                    idx[j] += 1

        return ugly[-1]