class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprofit=0
        minprices=prices[0]
        for i in range(1,len(prices)):
            maxprofit=max(maxprofit,prices[i]-minprices)
            minprices=min(minprices,prices[i])
        
        return maxprofit