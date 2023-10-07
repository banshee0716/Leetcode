class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7  # 用於取模
        
        # 初始化動態規劃陣列和前綴和
        dp = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prevDp = [[0] * (k+1) for _ in range(m+1)]
        prevPrefix = [[0] * (k+1) for _ in range(m+1)]
        
        # 初始化基礎情況
        for j in range(1, m+1):
            prevDp[j][1] = 1
            prevPrefix[j][1] = j
        
        # 從第2個位置開始計算，直到第n個位置
        for _ in range(2, n+1):
            dp = [[0] * (k+1) for _ in range(m+1)]
            prefix = [[0] * (k+1) for _ in range(m+1)]
            
            for maxNum in range(1, m+1):
                for cost in range(1, k+1):
                    # 如果當前數字等於前一個數字，則沒有增加新的升序區段
                    dp[maxNum][cost] = (maxNum * prevDp[maxNum][cost]) % mod
                    
                    # 如果當前數字大於前一個數字，則增加了新的升序區段
                    if maxNum > 1 and cost > 1:
                        dp[maxNum][cost] += prevPrefix[maxNum - 1][cost - 1]
                        dp[maxNum][cost] %= mod
                    
                    # 計算前綴和
                    prefix[maxNum][cost] = (prefix[maxNum - 1][cost] + dp[maxNum][cost]) % mod
            
            # 更新前一個位置的動態規劃陣列和前綴和
            prevDp, prevPrefix = [row[:] for row in dp], [row[:] for row in prefix]
        
        return prefix[m][k]

"""
這道題目是一個動態規劃問題。給定三個整數n、m和k，目標是計算出有多少種長度為n的數組，其中的數字介於1到m之間，並且其中有k個升序的區段。

我將為您解釋整個解題思路、加上詳細的註解，並最後以Black formatting整理後輸出。

解題思路：

1. 使用一個三維的動態規劃dp來存儲結果，其中dp[i][j][k]表示考慮前i個位置、最大值是j、並且具有k個升序區段的數組數量。
2. 為了方便計算，還需要一個前綴和prefix。
3. 利用先前計算的結果來計算當前位置的可能數組數量。

時間複雜度分析：
因為有三個循環，分別是n、m和k，所以時間複雜度為O(n×m×k)。

空間複雜度分析：
我們使用了固定大小的二維列表來存儲動態規劃的結果和前綴和，所以空間複雜度為O(m×k)。
"""