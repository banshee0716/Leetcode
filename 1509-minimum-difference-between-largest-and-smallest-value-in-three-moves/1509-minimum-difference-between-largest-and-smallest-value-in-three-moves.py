class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        min_diff = min(nums[n-1] - nums[3], nums[n-2] - nums[2], nums[n-3] - nums[1], nums[n-4] - nums[0])
        
        return min_diff
        
    
    """
給定一個整數數組 nums。

一步操作，可以選擇 nums 的一個元素並將其變更為任意值。

執行最多 3 次移動後，傳回 nums 的最大和最小值之間的最小差值。
    """