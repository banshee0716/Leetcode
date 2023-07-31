class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[i] - nums[i-1] for i in range(1,len(nums)))
"""
給定一個正整數數組 nums。

將 nums 劃分為兩個數組：nums1 和 nums2，這樣：

數組 nums 的每個元素屬於數組 nums1 或數組 nums2。
兩個數組都非空。
分區的值被最小化。
分區的值為 |max(nums1) - min(nums2)|。

這裡，max(nums1)表示數組nums1的最大元素，min(nums2)表示數組nums2的最小元素。

返回表示該分區值的整數。
"""