class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)-1
        ans = nums[n]
        
        #選擇一個整數 i，使得 0 <= i < nums.length - 1 且 nums[i] <= nums[i + 1]。
        #元素 nums[i + 1] 替換為 nums[i] + nums[i + 1] 並從數組中刪除元素 nums[i]。
        for i in range(n-1, -1, -1):
            ans = ans + nums[i] if nums[i] <= ans else nums[i]
            
        return ans
        
"""
給定一個由正整數組成的 0 索引數組 nums。

您可以對數組執行任意多次以下操作：

選擇一個整數 i，使得 0 <= i < nums.length - 1 且 nums[i] <= nums[i + 1]。將元素 nums[i + 1] 替換為 nums[i] + nums[i + 1] 並從數組中刪除元素 nums[i]。
返回最終數組中可能獲得的最大元素的值。
"""