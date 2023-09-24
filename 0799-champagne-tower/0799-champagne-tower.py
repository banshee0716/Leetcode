class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        # 初始化 dp 二維數組
        dp = [[0] * i for i in range(1, 102)]
        dp[0][0] = poured
        
        for i in range(100): # 可能的最大行數
            go_to_next_level = False # 這個標誌用於確定是否有杯子溢出
            for j in range(i + 1): 
                if dp[i][j] > 1: # 如果當前杯子香檳超過 1
                    go_to_next_level = True # 有杯子溢出
                    drip = dp[i][j] - 1 # 溢出的量
                    dp[i + 1][j] += drip / 2 # 均分到下面的左側杯子
                    dp[i + 1][j + 1] += drip / 2 # 均分到下面的右側杯子
                    dp[i][j] = 1 # 設置當前杯子的香檳為 1
                    
            # 若此輪沒有杯子溢出，則結束模擬
            if not go_to_next_level:
                break
        
        # 返回指定位置的杯子中的香檳量
        return dp[r][c]


"""
解題思路：
1. 創建一個二維數組 dp，其中 dp[i][j] 代表第 i 行第 j 列的杯子中的香檳量。
2. 首先將整個 poured 的量都倒入頂部的杯子。
3. 然後模擬香檳的流動。對於每個杯子，如果它的香檳量超過 1，那麼溢出的香檳會均分到下面的兩個杯子中。
4. 如果在某一輪模擬中，所有的杯子都沒有溢出，則模擬結束。

時間複雜度和空間複雜度：
時間複雜度：O(n^2)，其中 n 是行數。因為最差情況下，我們可能需要遍歷每個杯子。
空間複雜度：O(n^2)。
"""