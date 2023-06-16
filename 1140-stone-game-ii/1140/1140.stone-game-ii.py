#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#


# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # N為石頭堆的數量
        N = len(piles)
        # 定義動態規劃的數組dp
        self.dp = {}

        # 定義一個遞迴函數進行深度優先搜索
        def recursiveStoneGame(start, M):
            # 如果已經沒有石頭了，返回0
            if start >= N:
                return 0

            # 如果剩下的石頭數量小於等於2*M，則全部拿走
            if N - start <= 2 * M:
                return sum(piles[start:])

            # 如果已經計算過這個狀態，直接返回結果
            if (start, M) in self.dp:
                return self.dp[(start, M)]

            my_score = 0
            total_score = sum(piles[start:])
            # 嘗試所有可能的拿石頭的數量
            for x in range(1, 2 * M + 1):
                # 計算對手拿完石頭後的得分
                opponent_score = recursiveStoneGame(start + x, max(x, M))
                # 求最大的我方得分
                my_score = max(my_score, total_score - opponent_score)

            # 記錄這個狀態的結果
            self.dp[(start, M)] = my_score

            return my_score

        # 從起始狀態出發進行搜索
        return recursiveStoneGame(0, 1)


"""
這題也是一個遊戲策略問題，兩位玩家（Alex 和 Lee）輪流從一堆石頭中取走一定數量的石頭，
每次可以拿走的石頭數量範圍是1到2M個（M為上一輪取走石頭的數量），問最後Alex可以拿走多少石頭。

這個問題的解法主要是用深度優先搜索(DFS)和動態規劃(DP)的思路，
透過記錄中間計算結果避免重複計算，達到加速的效果
。我們從最開始的狀態出發，嘗試所有可能的走法，選擇最後能使我們拿到最多石頭的走法。
"""
"""
時間複雜度：
因為這個解法用了動態規劃來儲存中間結果，所以每個狀態只會計算一次，時間複雜度為O(n^2 * M)，其中n為石堆數量，M為可以拿取的最大石頭數量。

空間複雜度：
使用了動態規劃的數組來儲存結果，空間複雜度為O(n * M)，其中n為石堆數量，M為可以拿取的最大石頭數量。
"""
# @lc code=end
