class Solution:
    def maximumWeight(self, intervals):
        import bisect

        n = len(intervals)

        # end, start, weight, original index
        a = sorted(
            (r, l, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        ends = [x[0] for x in a]

        # dp[k][i] = best answer using first i intervals and at most k intervals
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):

                # Don't take current interval
                dp[k][i] = dp[k][i - 1]

                r, l, w, idx = a[i - 1]

                # Find previous interval with end < start
                p = bisect.bisect_left(ends, l, 0, i - 1)

                score, ids = dp[k - 1][p]

                new_score = score + w
                new_ids = sorted(ids + [idx])

                # Take current interval
                if new_score > dp[k][i][0]:
                    dp[k][i] = (new_score, new_ids)

                elif new_score == dp[k][i][0]:
                    if new_ids < dp[k][i][1]:
                        dp[k][i] = (new_score, new_ids)

        return dp[4][n][1]