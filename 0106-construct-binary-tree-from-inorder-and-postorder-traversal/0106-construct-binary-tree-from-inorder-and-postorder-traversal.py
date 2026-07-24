class Solution:
    def buildTree(self, inorder, postorder):
        pos = {v: i for i, v in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            idx = pos[val]

            root.right = build(idx + 1, right)
            root.left = build(left, idx - 1)

            return root

        return build(0, len(inorder) - 1)