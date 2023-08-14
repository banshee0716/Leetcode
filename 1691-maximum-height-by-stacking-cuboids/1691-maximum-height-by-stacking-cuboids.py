class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 首先對每個矩形方塊進行排序，確保長度、寬度、高度的順序
        for cuboid in cuboids:
            cuboid.sort()

        # 接著對整體的矩形方塊進行排序
        cuboids.sort()
        n = len(cuboids)
        # 初始化dp列表，該列表表示以某個矩形方塊為基礎的最大高度
        dp = [height for _, _, height in cuboids]

        # 從後往前遍歷每個矩形方塊
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 檢查cuboids[i]是否可以放在cuboids[j]的上面
                if (
                    cuboids[i][1] <= cuboids[j][1]
                    and cuboids[i][2] <= cuboids[j][2]
                ):
                    # 更新dp[i]為它自己的高度或者加上dp[j]後的最大值
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])

        # 返回dp列表中的最大值，這是答案
        return max(dp)

        
"""
解題思路：

1. 首先，我們要確保每個矩形方塊的長度、寬度和高度是按照順序的，所以我們對它們進行排序。
2. 然後，對整體的矩形方塊進行排序，這樣我們可以確保後面的矩形方塊至少在一個維度上大於或等於前面的。
3. 我們使用動態規劃的策略來計算以每個矩形方塊為基礎的最大高度。通過從後往前遍歷每個矩形方塊，我們確保了後面的矩形方塊已經被計算過。

時間複雜度：O(n^2)，其中n是矩形方塊的數量。這是因為我們對每一對矩形方塊都進行了比較。
空間複雜度：O(n)，因為我們使用了一個大小為n的dp列表來存儲結果。
"""