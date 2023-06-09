#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        return sorted(P, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


# @lc code=end
