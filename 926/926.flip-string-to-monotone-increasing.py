#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # ones 變量表示目前字符串中的 1 的個數，res 變量表示最少需要翻轉幾個字符
        ones, res = 0, 0
        # 遍歷字符串
        for num in s:
            # 如果當前字符是 1，就增加 ones 變量
            if num == "1":
                ones += 1
            # 如果當前字符是 0，表示需要把這個字符翻轉成 1，但是不是所有的 0 都需要翻轉
            # 我們只需要翻轉前面出現的 1 的個數即可，因為後面的 1 翻轉成 0 之後肯定會再翻轉回去
            elif ones:
                res += 1
                ones -= 1

        # 返回最少需要翻轉幾個字符
        return res



# @lc code=end
