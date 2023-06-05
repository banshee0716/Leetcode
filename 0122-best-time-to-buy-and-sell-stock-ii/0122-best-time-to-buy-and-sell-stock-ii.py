class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache   # 使用 cache 修飾器來儲存每一天的最佳狀態，避免重複運算
        def trade(day_d):
            
            if day_d == 0:  # 遞歸終止條件：當天數等於0
                return -prices[day_d], 0  # 持有股票和不持有股票的兩種狀態
            
            # 獲得前一天的持有股票和不持有股票的狀態
            prev_hold, prev_not_hold = trade(day_d-1)
            
            # 當天的持有股票狀態，可以從前一天的持有股票狀態來，或者前一天不持有股票但是當天購買股票
            hold = max(prev_hold, prev_not_hold - prices[day_d] )
            
            # 當天的不持有股票狀態，可以從前一天的不持有股票狀態來，或者前一天持有股票但是當天賣出股票
            not_hold = max(prev_not_hold, prev_hold + prices[day_d] )
            
            return hold, not_hold  # 返回當天的最佳狀態
        
        last_day= len(prices)-1  # 計算出最後一天的索引值
        
        return trade(last_day)[1]  # 返回最後一天不持有股票的狀態（即最大利潤）
"""

時間複雜度：O(n)，其中 n 是價格數組的長度。我們需要遍歷整個價格數組。

空間複雜度：O(n)。儘管遞歸需要消耗額外的空間，但由於 Python 中的緩存（cache）機制，我們可以把時間換空間，只需儲存每天的狀態。因此空間複雜度也是 O(n)。
"""