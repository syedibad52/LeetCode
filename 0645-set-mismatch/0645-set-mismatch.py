class Solution:
    def findErrorNums(self, nums):
        s = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in s:
                missing = i
                break

        duplicate = sum(nums) - sum(s)

        return [duplicate, missing]