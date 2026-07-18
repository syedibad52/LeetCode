class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                s = mul + res[i + j + 1]
                res[i + j + 1] = s % 10
                res[i + j] += s // 10

        ans = ""
        for x in res:
            if not (ans == "" and x == 0):
                ans += str(x)

        return ans