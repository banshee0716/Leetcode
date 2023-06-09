#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for num in nums:
            if d[num]:
                return num
            else:
                d[num] = 1


# @lc code=end
