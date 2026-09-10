class Solution:
    def averageOfSubtree(self, root):
        ans = [0]

        def dfs(node):
            if not node:
                return 0, 0

            s1, c1 = dfs(node.left)
            s2, c2 = dfs(node.right)

            s = s1 + s2 + node.val
            c = c1 + c2 + 1

            if node.val == s // c:
                ans[0] += 1

            return s, c

        dfs(root)
        return ans[0]