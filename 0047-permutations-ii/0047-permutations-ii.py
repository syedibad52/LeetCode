class Solution:
    def permuteUnique(self, nums):
        res = []

        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return

            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                backtrack(path + [arr[i]], arr[:i] + arr[i+1:])

        nums.sort()
        backtrack([], nums)
        return res