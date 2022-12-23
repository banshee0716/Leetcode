
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = [0] * len(prices)
        s = [0] * len(prices)
        b[0] = -prices[0]
        for i in range(1, len(prices)):
            b[i] = max(b[i - 1], s[i - 2] - prices[i])
            s[i] = max(s[i - 1], b[i - 1] + prices[i])
        return s[-1]