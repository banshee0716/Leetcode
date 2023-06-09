#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:

        num = sorted(list(str(num)))
        num1, num2 = int("".join(num[0::2])), int("".join(num[1::2]))
        return num1 + num2


# @lc code=end
