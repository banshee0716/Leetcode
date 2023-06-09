#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i != "*":
                res.append(i)
            else:
                res.pop()
        # return str(res)
        return "".join(res)


# @lc code=end
