#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 使用functools.lru_cache實現動態規劃，緩存中間結果提高效率
        @lru_cache(None)
        def dp(i, j):
            # 當s遍歷結束時，只有t也遍歷結束才算一種匹配方案
            if i == -1:
                return j == -1
            # 當t遍歷結束時，s仍有剩餘字符，不可能匹配成功，返回0
            if j == -1:
                return j == -1
            # 根據是否匹配來遞歸計算匹配方案數，s[i] == t[j]時有兩種選擇：匹配或不匹配
            return dp(i - 1, j) + (s[i] == t[j]) * dp(i - 1, j - 1)

        # 返回s和t之間的匹配方案數
        return dp(len(s) - 1, len(t) - 1)


"""該程式使用動態規劃求解s和t之間的匹配方案數，
其中 dp(i, j) 表示將 s[0:i] 轉化為 t[0:j] 的匹配方案數，
使用 Python 中的 functools.lru_cache 實現緩存，避免重複運算。
當 i == -1 時，只有當 j == -1 才算一種匹配方案；當 j == -1 時，表示 t 遍歷完畢，此時如果 s 還有剩餘字符，匹配必然失敗，返回 0；
否則，根據是否匹配來計算匹配方案數，如果 s[i] == t[j]，則有兩種選擇：匹配或不匹配。
最終返回 s 和 t 之間的匹配方案數，即 dp(len(s) - 1, len(t) - 1)。"""


"""時間複雜度：O(len(s) * len(t))
因為程式中使用了一個帶有緩存的遞迴函數來計算結果，該遞迴函數的時間複雜度為O(len(s) * len(t))，因為它需要遍歷s和t中的每個字符。

空間複雜度：O(len(s) * len(t))
由於使用了緩存來儲存中間結果，因此空間複雜度與時間複雜度相同。"""
# @lc code=end
