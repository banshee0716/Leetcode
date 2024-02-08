class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化DP表
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 0可以由0個完全平方數相加得到
        
        # 填充DP表
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            
            # 嘗試減去一個完全平方數並更新最小值
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        
        # 返回組成n所需的最少完全平方數的數量
        return dp[n]

    
    """
解題思路
這個問題可以通過動態規劃（Dynamic Programming, DP）來解決。基本思想是構建一個DP表dp，其中dp[i]表示整數i由最少的完全平方數相加組成的數量。

初始化DP表：
    -初始化dp表的大小為n+1，所有值設置為float('inf')（無窮大），代表初始時沒有任何數字可以由完全平方數的和組成。將dp[0]設為0，因為0可以由0個完全平方數相加得到。

填充DP表：
    -從1遍歷到n，對於每個數i，嘗試減去一個完全平方數j*j，查找最少的完全平方數的和的個數。這裡j從1開始，直到j*j小於等於i為止。

返回結果：
    -最終dp[n]中存儲的就是組成n所需的最少完全平方數的數量。
    
時間複雜度
    -外層循環從1遍歷到n，內層循環在最壞情況下遍歷到sqrt(n)。因此，總的時間複雜度為O(n*sqrt(n))。
    
空間複雜度
    -由於使用了一個長度為n+1的DP表，因此空間複雜度為O(n)。
    """