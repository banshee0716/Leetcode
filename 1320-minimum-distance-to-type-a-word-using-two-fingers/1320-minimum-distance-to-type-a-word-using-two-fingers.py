class Solution(object):
    def minimumDistance(self, A):
        def d(a, b):
            return a and abs(a / 6 - b / 6) + abs(a % 6 - b % 6)

        dp, dp2 = {(0, 0): 0}, {}
        for c in (ord(c) + 1 for c in A):
            for a, b in dp:
                dp2[c, b] = min(dp2.get((c, b), 3000), dp[a, b] + d(a, c))
                dp2[a, c] = min(dp2.get((a, c), 3000), dp[a, b] + d(b, c))
            dp, dp2 = dp2, {}
        return min(dp.values())