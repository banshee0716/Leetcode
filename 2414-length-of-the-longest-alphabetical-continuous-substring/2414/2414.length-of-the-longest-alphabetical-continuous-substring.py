#
# @lc app=leetcode id=2414 lang=python3
#
# [2414] Length of the Longest Alphabetical Continuous Substring
#

# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt, res = 1, 1

        for idx in range(1, len(s)):
            if ord(s[idx]) - ord(s[idx - 1]) == 1:
                cnt += 1
            else:
                cnt = 1

            res = max(res, cnt)

        return res


# @lc code=end
