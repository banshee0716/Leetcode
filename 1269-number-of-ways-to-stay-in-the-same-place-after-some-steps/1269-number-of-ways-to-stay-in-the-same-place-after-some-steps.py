class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # m為總步數，n為可以移動到的最大位置
        m = steps
        n = min(steps // 2 + 1, arrLen)  # 考慮最遠可能移動的距離

        # 初始化動態規劃表
        dp = [[0] * n for _ in range(m + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7  # 用於取模的數值

        # 更新動態規劃表
        for i in range(1, m + 1):
            for j in range(n):
                # 不移動的情況
                dp[i][j] = dp[i-1][j]
                # 如果可以向左移動
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                # 如果可以向右移動
                if j < n - 1:
                    dp[i][j] += dp[i-1][j+1]
        
        # 回傳最後的結果，並取模以確保不超過10^9 + 7
        return dp[m][0] % mod

"""
計算出有多少種方式，使得一個位置在一開始時位於位置0，經過指定的步數後，再次回到位置0。這個位置每一步可以向左、向右或者不移動。此外，還有一個陣列的長度arrLen限制它能移動到的最大位置。

解題思路：
1. 使用動態規劃來解決這個問題。
2. 定義dp[i][j]表示在i步後到達位置j的方式數量。
3. 考慮三種可能的移動：左、右和不移動。對於每一種移動，我們都從前一步更新它的值。

時間複雜度：
時間複雜度是O(steps×min(steps,arrLen))，因為我們需要遍歷每一步和每一個可能的位置。
空間複雜度：
空間複雜度是O(steps×min(steps,arrLen))，因為我們需要為動態規劃表分配空間。
"""