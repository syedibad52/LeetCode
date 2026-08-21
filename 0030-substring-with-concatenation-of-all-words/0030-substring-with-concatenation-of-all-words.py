class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        w = len(words[0])
        n = len(words)
        need = Counter(words)
        ans = []

        for start in range(w):
            left = start
            count = 0
            seen = {}

            for right in range(start, len(s) - w + 1, w):
                word = s[right:right+w]

                if word not in need:
                    seen = {}
                    count = 0
                    left = right + w
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > need[word]:
                    old = s[left:left+w]
                    seen[old] -= 1
                    left += w
                    count -= 1

                if count == n:
                    ans.append(left)

        return ans