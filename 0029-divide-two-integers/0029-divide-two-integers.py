class Solution:
    def divide(self, dividend, divisor):
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            ans += multiple

        return ans if sign > 0 else -ans