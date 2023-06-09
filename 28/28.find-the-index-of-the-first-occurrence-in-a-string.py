#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end = len(needle)
        for i in range(len(haystack)):
            if haystack[i:end] == needle:
                return i
            end += 1
        return -1


"""
api解
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
"""


# @lc code=end
