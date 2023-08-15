class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 如果cost為空，直接返回0
        if not cost:
            return 0
        
        n = len(cost)
        # dp[i]表示到達第i階梯所需的最小費用
        dp = [0] * n
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        
        # 開始動態規劃
        # 對於每一階，計算到達該階梯的最小費用
        for i in range(2, n):
            # 到達第i階的最小費用是當前階的費用加上前一階和前兩階的最小值
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # 因為可以從最後一階或倒數第二階達到頂部，所以返回這兩者的最小值
        return min(dp[-1], dp[-2])


    """
解題思路：

創建一個dp陣列，其每一項dp[i]代表到達第i階梯所需的最小費用。
初始化dp[0]和dp[1]。
使用動態規劃填充dp陣列，其中每一項的值是當前階梯的費用加上前一階和前兩階的最小值。
因為可以從最後一階或倒數第二階直接到達頂部，所以最後返回dp[-1]和dp[-2]中的最小值。

時間複雜度：O(n)，其中n是給定的階梯數量，因為我們只遍歷階梯一次。
空間複雜度：O(n)，我們需要一個長度為n的dp陣列來存儲每個階梯的最小成本。
    """