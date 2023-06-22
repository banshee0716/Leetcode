class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b, s = inf, 0
        for p in prices:
            b = min(b, p - s)
            s = max(s, p - b - fee)
        return s