#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        # 初始化一個長度為 n 的動態規劃列表 dp
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            # 初始化 prev 變量，用於記錄 dp[j-1] 的值
            prev = 0
            # 遍歷 s[i+1] 到 s[n-1] 的字符
            for j in range(i + 1, n):
                # 保存當前 dp[j] 的值
                temp = dp[j]

                # 如果 s[i] 等於 s[j]，則 dp[j] 等於 prev
                if s[i] == s[j]:
                    dp[j] = prev
                # 否則，dp[j] 等於 dp[j] 和 dp[j-1] 中的最小值加 1
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1

                # 更新 prev 的值
                prev = temp

        # 返回 dp[n-1]，即最少插入次數
        return dp[n - 1]


"""
時間複雜度分析：

1. 遍歷字符串 s 的時間複雜度為 O(n)，其中 n 為字符串 s 的長度。
2. 遍歷 s[i+1] 到 s[n-1] 的字符的時間複雜度為 O(n)。
綜合以上分析，此算法的總時間複雜度為 O(n^2)。

空間複雜度分析：

1. 動態規劃列表 dp 的空間複雜度為 O(n)。
綜合以上分析，此算法的總空間複雜度為 O(n)。
"""
# @lc code=end
