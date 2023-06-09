#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#


# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 初始化 dp 列表，將其所有值設置為0
        dp = [0] * (high + 1)
        # 初始值設置為1，表示 "" 為一個好字符串
        dp[0] = 1
        # 取模常數
        md = 10**9 + 7

        # 遍歷 0 和 1 的數量範圍，更新 dp 列表
        for i in range(min(zero, one), high + 1):
            if i >= zero:
                # 更新 dp[i]，加上 dp[i-zero] 的值
                dp[i] = (dp[i] + dp[i - zero]) % md
            if i >= one:
                # 更新 dp[i]，加上 dp[i-one] 的值
                dp[i] = (dp[i] + dp[i - one]) % md

        # 遍歷範圍 low 到 high，計算 dp[i] 的總和
        s = 0
        for i in range(low, high + 1):
            s = (s + dp[i]) % md

        # 返回結果
        return s


"""
時間複雜度：o(n)
空間複雜度：o(n)
"""

# @lc code=end
