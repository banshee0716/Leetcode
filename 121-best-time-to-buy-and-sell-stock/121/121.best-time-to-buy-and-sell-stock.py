#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 如果列表為空則沒有交易機會，利潤為0
        if not prices:
            return 0

        maxProfit = 0  # 定義最大利潤初始值為0
        minPrice = prices[0]  # 定義最小價格初始值為第一個元素

        # 從第二個元素開始遍歷列表
        for i in range(1, len(prices)):
            # 計算當前利潤和最大利潤的較大值
            maxProfit = max(maxProfit, prices[i] - minPrice)
            # 計算當前最小價格和最小價格的較小值
            minPrice = min(minPrice, prices[i])

        # 返回最大利潤
        return maxProfit


# 時間複雜度是O(n)，其中n是股票價格列表中元素的數量。這是因為程式只遍歷一次股票價格列表。
# 空間複雜度是O(1)，因為程式只使用了常數額外的空間。

# @lc code=end
