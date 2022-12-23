class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0] #
        for i in range(1,len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            
        return sell[-1]
            
            
            
        #After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).