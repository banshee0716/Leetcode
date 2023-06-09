#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#

# @lc code=start
import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(x, i) for i, x in enumerate(nums)]  # min-heap
        heapq.heapify(h)

        ans = 0
        for k in range(1, right + 1):  # 1-indexed
            x, i = heapq.heappop(h)
            if k >= left:
                ans += x
            if i + 1 < len(nums):
                heapq.heappush(h, (x + nums[i + 1], i + 1))

        return ans % 1_000_000_007


# @lc code=end
