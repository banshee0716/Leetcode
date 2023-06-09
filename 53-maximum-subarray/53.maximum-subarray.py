#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 遍歷數組，當前位置上的數字加上前一個位置上的數字，若和大於當前位置的數字，則把和賦給當前位置上的數字
        # 如果和小於等於當前位置的數字，則不變化，即保持原值
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)


"""
時間複雜度：此算法遍歷了一次數組，因此時間複雜度為O(n)。
空間複雜度：此算法只使用了常數級別的額外空間，因此空間複雜度為O(1)。
"""

# @lc code=end
