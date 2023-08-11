class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 初始化 dp 陣列，大小為 amount+1。每個值初始化為0。
        dp = [0] * (amount+1)
        
        # 有一種方法可以組成金額0，那就是不使用任何硬幣。
        dp[0] = 1
        
        # 對於每一種硬幣
        for coin in coins:
            # 使用這個硬幣可以組成的所有可能的金額
            for j in range(coin, amount+1):
                # dp[j] 被更新為 dp[j]（不使用這個硬幣的組合數）+ dp[j - coin]（使用這個硬幣的組合數）。
                dp[j] += dp[j - coin]
                
        # dp[amount] 是組成金額 amount 的組合數。
        return dp[amount]

                
        
"""
https://leetcode.com/problems/coin-change-ii/discuss/3892702/100-Dynamic-Programming-VIDEO-Optimal-Solution

1. 使用一個陣列 dp 來紀錄每個金額的組合數。
2. 遍歷每一種硬幣，對於每一種硬幣，遍歷它可以組成的所有金額，更新這些金額的組合數。

時間複雜度：O(amount * len(coins))，因為我們需要遍歷每一種硬幣，並更新使用這個硬幣可以組成的每個金額的組合數。
空間複雜度：O(amount)，我們只需要一個大小為 amount+1 的陣列來儲存組合數。
"""