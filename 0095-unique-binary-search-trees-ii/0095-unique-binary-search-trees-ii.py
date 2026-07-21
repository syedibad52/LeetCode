class Solution:
    def generateTrees(self, n):
        def build(start, end):
            if start > end:
                return [None]

            res = []

            for i in range(start, end + 1):
                left = build(start, i - 1)
                right = build(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res

        return build(1, n)