class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        one = ["", "One", "Two", "Three", "Four", "Five",
               "Six", "Seven", "Eight", "Nine"]
        ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
               "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        def solve(n):
            if n < 10:
                return one[n]
            if n < 20:
                return ten[n - 10]
            if n < 100:
                return tens[n // 10] + (" " + one[n % 10] if n % 10 else "")
            return one[n // 100] + " Hundred" + (" " + solve(n % 100) if n % 100 else "")

        ans = []

        if num >= 1000000000:
            ans += [solve(num // 1000000000), "Billion"]
            num %= 1000000000

        if num >= 1000000:
            ans += [solve(num // 1000000), "Million"]
            num %= 1000000

        if num >= 1000:
            ans += [solve(num // 1000), "Thousand"]
            num %= 1000

        if num:
            ans.append(solve(num))

        return " ".join(ans)