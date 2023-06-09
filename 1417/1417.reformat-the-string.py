#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""

        rv = []
        flag = len(letters) > len(digits)
        while letters or digits:
            rv.append(letters.pop() if flag else digits.pop())
            flag = not flag
        return rv


# @lc code=end
