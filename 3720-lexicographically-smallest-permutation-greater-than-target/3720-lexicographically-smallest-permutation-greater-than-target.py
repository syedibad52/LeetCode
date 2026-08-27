class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - 97

            # Try to keep same character
            if cnt[x]:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Need a bigger character
                for j in range(x + 1, 26):
                    if cnt[j]:
                        ans.append(chr(j + 97))
                        cnt[j] -= 1
                        return ''.join(ans) + ''.join(
                            chr(k + 97) * cnt[k] for k in range(26)
                        )

                # Backtrack
                while ans:
                    old = ord(ans.pop()) - 97
                    cnt[old] += 1

                    for j in range(old + 1, 26):
                        if cnt[j]:
                            ans.append(chr(j + 97))
                            cnt[j] -= 1
                            return ''.join(ans) + ''.join(
                                chr(k + 97) * cnt[k] for k in range(26)
                            )

                return ""

        # s permutation == target, so backtrack
        while ans:
            old = ord(ans.pop()) - 97
            cnt[old] += 1

            for j in range(old + 1, 26):
                if cnt[j]:
                    ans.append(chr(j + 97))
                    cnt[j] -= 1
                    return ''.join(ans) + ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )

        return ""