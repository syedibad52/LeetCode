class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        d = {}

        def dfs(node):
            if node in d:
                return d[node]

            copy = Node(node.val)
            d[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)