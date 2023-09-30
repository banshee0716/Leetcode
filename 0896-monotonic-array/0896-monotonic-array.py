class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            inc = inc and nums[i-1] >= nums[i]
            dec = dec and nums[i-1] <= nums[i]
            
        return inc or dec
            