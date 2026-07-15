from collections import Counter

class Solution:
    def topKFrequent(self, num, k):
        c = Counter(num)
        return [x for x, _ in c.most_common(k)]