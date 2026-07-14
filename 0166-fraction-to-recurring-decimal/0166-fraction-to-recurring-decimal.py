class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        ans = ""

        if (numerator < 0) != (denominator < 0):
            ans += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        ans += str(numerator // denominator)
        rem = numerator % denominator

        if rem == 0:
            return ans

        ans += "."
        seen = {}

        while rem:
            if rem in seen:
                i = seen[rem]
                ans = ans[:i] + "(" + ans[i:] + ")"
                break

            seen[rem] = len(ans)
            rem *= 10
            ans += str(rem // denominator)
            rem %= denominator

        return ans