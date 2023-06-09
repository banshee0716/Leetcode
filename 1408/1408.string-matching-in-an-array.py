#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = " ".join(words)
        subStr = [i for i in words if arr.count(i) >= 2]

        return subStr


# @lc code=end
