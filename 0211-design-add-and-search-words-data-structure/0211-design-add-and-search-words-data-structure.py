class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]

        node.end = True

    def search(self, word):

        def dfs(i, node):
            if i == len(word):
                return node.end

            ch = word[i]

            if ch == '.':
                for nxt in node.child.values():
                    if dfs(i + 1, nxt):
                        return True
                return False

            if ch not in node.child:
                return False

            return dfs(i + 1, node.child[ch])

        return dfs(0, self.root)