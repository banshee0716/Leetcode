from typing import List, Set

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        # 創建一個哈希表，key 是石頭的位置，value 是一個集合，存儲到達該位置可能的跳躍距離。
        dp = {stone: set() for stone in stones}
        # 初始化起點，跳躍距離為 0
        dp[0].add(0)
        
        # 遍歷每個石頭
        for i in range(n):
            # 遍歷到達該石頭的所有可能的跳躍距離
            for k in dp[stones[i]]:
                # 計算下一次可能的跳躍距離
                for step in range(k - 1, k + 2):
                    # 確保跳躍距離為正數，並且下一個位置存在於石頭列表中
                    if step > 0 and stones[i] + step in dp:
                        # 更新哈希表
                        dp[stones[i] + step].add(step)
        
        # 檢查是否能到達最後一塊石頭
        return len(dp[stones[-1]]) > 0
"""

這個題目是一個動態規劃問題，主要是要判斷青蛙能否跳過一個由石頭組成的河流。每次跳躍的距離不能夠相等，但可以是上一次跳躍距離的 -1、0 或 +1。也就是說，如果上一次跳躍了 k 單位，下一次可以跳躍 k-1、k 或 k+1 單位。

解題思路
1. 創建一個哈希表 dp 來存儲每個石頭位置和到達該位置時可能的跳躍距離。
2. 初始化 dp[0] 為一個只含有一個元素 0 的集合。
3. 使用嵌套的迴圈來遍歷每個石頭和每個可能的跳躍距離 k。
4. 基於 k 來更新下一個可達的石頭位置。

時間複雜度：O(n^2)，其中 n 是石頭的數量。這是因為我們需要遍歷每個石頭和每個石頭上可能的跳躍距離。
空間複雜度：O(n)，這裡也是石頭的數量，因為我們使用了一個哈希表來存儲信息。
"""