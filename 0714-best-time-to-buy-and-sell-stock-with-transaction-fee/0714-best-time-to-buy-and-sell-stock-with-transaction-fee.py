

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        # 如果價格陣列的長度小於2，則無法進行交易，直接返回0
        if n < 2:
            return 0
        
        # 初始化答案為0
        ans = 0
        # 初始化最小價格為陣列的第一個元素
        minimum = prices[0]
        
        for i in range(1, n):
            # 如果當前價格小於最小價格，則更新最小價格
            if prices[i] < minimum:
                minimum = prices[i]
                
            # 如果當前價格大於最小價格加上費用，則進行交易
            elif prices[i] > minimum + fee:
                # 更新總利潤
                ans += prices[i] - fee - minimum
                # 更新最小價格為交易後的價格
                minimum = prices[i] - fee
                
        return ans  # 返回最大利潤
    
"""
貪婪算法來解決。每次買賣都需要支付一定的費用，我們需要找到一個最小的價格來購買股票，然後找一個價格高於最小價格加上費用的價格來賣出，這樣可以保證賺取的利潤最大化。
這個程式碼的時間複雜度為 O(n)，其中 n 是價格陣列的長度。我們需要遍歷每個價格來決定是否進行交易。

空間複雜度為 O(1)。我們只需要一個變數來存儲最小價格，並不需要額外的空間來存儲其他資訊。
"""



