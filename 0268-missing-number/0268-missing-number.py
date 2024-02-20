class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        m = min(nums)
        for i in range(m, l+1):
            if i not in nums:
                return i
        
        return 0