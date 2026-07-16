from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def cmp(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(cmp))
        ans = "".join(nums)

        return "0" if ans[0] == "0" else ans