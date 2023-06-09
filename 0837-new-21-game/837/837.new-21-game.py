#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#


# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 如果 k 為 0，或者 n 大於等於 k + maxPts，則獲勝的機率為 100%
        if k == 0 or n >= k + maxPts:
            return 1.0

        # 初始化滑動窗口的和（存儲 maxPts 個最近的 dp 值的和）和獲勝的機率
        windowSum = 1.0
        probability = 0.0

        # dp[i] 表示從 0 點開始，玩到點數 i 的機率
        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        # 對於每一個可能的點數 i
        for i in range(1, n + 1):
            # 由於獲得點數是均勻分布，所以玩到點數 i 的機率是最近 maxPts 個機率的平均值
            dp[i] = windowSum / maxPts

            # 如果點數還不到 k，則將當前的 dp[i] 加到窗口的和中
            if i < k:
                windowSum += dp[i]
            else:
                # 否則，將當前的 dp[i] 加到獲勝的機率中
                probability += dp[i]

            # 如果點數超過 maxPts，則將窗口的最左邊的 dp[i - maxPts] 減去
            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        # 返回最後的獲勝機率
        return probability


"""
題目描述了一個點數賭博遊戲，其中點數最大不超過 n，玩家在點數小於 k 時會選擇繼續賭博，獲得的點數在 1 到 maxPts 之間隨機分布。我們需要求的是玩家點數不超過 n 的機率。

這個問題可以用動態規劃 (Dynamic Programming, DP) 的方式來求解。DP 是一種特殊的優化算法，常用於解決具有重疊子問題和最優子結構的問題。
在這個問題中，我們可以將每一步的獲勝機率作為子問題，逐步推導出終點的獲勝機率。
"""
"""
時間複雜度：
這個程式碼的時間複雜度是 O(n)，因為需要對每一個可能的點數計算其機率。而且在每一次迴圈中，所有操作都是 O(1) 的。

空間複雜度：
這個程式碼的空間複雜度也是 O(n)，主要消耗在 dp 陣列上。這個陣列需要存儲從 0 到 n 的所有點數的機率。
"""
# @lc code=end
