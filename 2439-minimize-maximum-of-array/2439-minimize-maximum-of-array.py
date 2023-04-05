class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total_sum, result = 0, 0
        for index in range(len(nums)):
            total_sum += nums[index]
            result = max(result, (total_sum + index) // (index + 1))
            
        return int(result)
            
    
    #執行任意次數的操作後，返回 nums 的最大整數的最小可能值。