class Solution:
    def majorityElement(self, nums):
        a = b = None
        c1 = c2 = 0

        for x in nums:
            if x == a:
                c1 += 1
            elif x == b:
                c2 += 1
            elif c1 == 0:
                a, c1 = x, 1
            elif c2 == 0:
                b, c2 = x, 1
            else:
                c1 -= 1
                c2 -= 1

        return [x for x in (a, b) if nums.count(x) > len(nums) // 3]