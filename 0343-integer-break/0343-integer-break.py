class Solution:
    def integerBreak(self, n: int) -> int:
        # 創建一個陣列保存從0到6的數的最大乘積
        case = [0, 0, 1, 2, 4, 6, 9]
        if n < 7:
            # 如果n小於7，則直接從case陣列中返回結果
            return case[n]
        # 對於大於6的n，擴展dp陣列並初始化為0
        dp = case + [0] * (n - 6)
        for i in range(7, n + 1):
            # 更新dp[i]，dp[i-3]*3是當前最大乘積
            dp[i] = 3 * dp[i - 3]
        
        # 返回最後一個元素，即整數n的最大乘積
        return dp[-1]
    
"""
時間複雜度是 O(n)，因為我們需要填充 dp 陣列，需要迭代從7到n的所有數字。
空間複雜度也是 O(n)，因為我們需要一個大小為 n 的 dp 陣列來儲存子問題的解。
"""