#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
"""
给定一个整数数组nums和两个整数minK和maxK。

一个fixed-bound子数组是一个满足以下条件的子数组：

子数组中的最小值等于minK。
子数组中的最大值等于maxK。
返回fixed-bound子数组的数量。

子数组是数组的连续一部分。"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # 初始化變數
        result = 0  # fixed-bound subarray 的個數
        left_index = right_index = bad_index = -1

        for i, num in enumerate(nums):
            # 判斷 num 是否在 [minK, maxK] 區間之外
            if not minK <= num <= maxK:
                bad_index = i  # 更新 bad_index 為 i
            # 判斷 num 是否為 minK
            if num == minK:
                left_index = i  # 更新 left_index 為 i
            # 判斷 num 是否為 maxK
            if num == maxK:
                right_index = i  # 更新 right_index 為 i
            # 計算 fixed-bound subarray 的個數
            result += max(0, min(left_index, right_index) - bad_index)

        return result


"""
時間複雜度：遍歷 nums 列表，所以算法的時間複雜度為 O(n)，其中 n 是列表 nums 的長度。

空間複雜度：算法使用常數額外空間存儲變量，因此空間複雜度為 O(1)。
"""
# @lc code=end
