#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        # 定義動態規劃函數
        @lru_cache(None)
        def dp(i, j):
            # 當其中一個字串為空時，需要刪除或插入所有字符才能匹配，返回剩餘長度
            if i == 0:
                return j  # Need to insert j chars
            if j == 0:
                return i  # Need to delete i chars
            # 如果當前字符相同，則無需操作，考慮下一個字符
            if s1[i - 1] == s2[j - 1]:
                return dp(i - 1, j - 1)
            # 否則分別考慮刪除s1的當前字符、刪除s2的當前字符或替換s1的當前字符為s2的當前字符
            return min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1

        # 調用動態規劃函數，返回s1和s2之間的最小距離
        return dp(len(s1), len(s2))


"""程式碼解析與時間複雜度：

使用動態規劃求解最小編輯距離，使用了一個 LRU Cache 進行記憶化，避免重複計算。
dp(i, j) 代表將 s1 前 i 個字符轉化為 s2 前 j 個字符需要的最小編輯距離。
當 s1 的第 i 個字符等於 s2 的第 j 個字符時，不需要進行修改，直接返回 dp(i-1, j-1)。
否則，需要考慮三種情況：
刪除 s1 的第 i 個字符，即 dp(i-1, j)；
插入 s2 的第 j 個字符，即 dp(i, j-1)；
將 s1 的第 i 個字符修改為 s2 的第 j 個字符，即 dp(i-1, j-1)。
最終返回 dp(len(s1), len(s2)) 即可得到最小編輯距離。
時間複雜度：由於使用了 LRU Cache 進行記憶化，每個狀態最多只會被計算一次，所以時間複雜度為 O(mn)，其中 m 和 n 分別是 s1 和 s2 的長度。
空間複雜度：使用了 LRU Cache 進行記憶化，所以空間複雜度為 O(mn)。"""

# @lc code=end
