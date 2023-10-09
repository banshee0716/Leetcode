class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = n * [1]
        for i in range(1, n):
            if prices[i] == prices[i-1]-1:
                dp[i] = 1+dp[i-1]
                
        return sum(dp)
                 
"""
使得每天的價格比前一天的價格剛好低 1
"""