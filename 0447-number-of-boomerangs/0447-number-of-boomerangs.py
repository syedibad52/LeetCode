class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0

        for i in points:
            d = {}
            for j in points:
                dis = (i[0]-j[0])**2 + (i[1]-j[1])**2
                d[dis] = d.get(dis, 0) + 1

            for x in d.values():
                ans += x * (x - 1)

        return ans