from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        
        # 初始化dp陣列
        dp = [1] * n
        for i in range(1, n):
            # 檢查當前價格是否是前一天減1
            if prices[i] == prices[i - 1] - 1:
                dp[i] = 1 + dp[i - 1]
        
        # 回傳平滑下降期的總數
        return sum(dp)

                 
"""
題目描述了一個股票的日價歷史，我們需要計算所有平滑下降期的數量。
平滑下降期表示股價連續下降，每天下降的幅度都是1，第一天除外（因為沒有前一天來比較）。

解題思路：
1. 我們首先創建一個動態規劃的陣列 dp 來儲存每一天結束時的平滑下降期的長度。
2. 初始化 dp 的每個元素為1。
3. 遍歷 prices，從第二天開始，若當前價格是前一天價格減1，則更新 dp[i] 以累積當前的平滑下降期的長度。
4. 最後返回 dp 陣列的總和，這是因為每次下降1都會對應於一個平滑下降期。

時間複雜度分析：
我們只遍歷了一次 prices 陣列，所以時間複雜度是O(n)，其中 n 是 prices 陣列的長度。

空間複雜度分析：
我們使用了一個額外的陣列 dp 來儲存平滑下降期的長度，因此空間複雜度是 O(n)。
"""