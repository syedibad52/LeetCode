class Solution:
    def isValidSerialization(self, preorder):
        slots = 1

        for x in preorder.split(','):
            if slots == 0:
                return False

            if x == '#':
                slots -= 1
            else:
                slots += 1

        return slots == 0