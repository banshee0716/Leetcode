class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n+1):
            if n % i == 0:
                ans += nums[i-1]**2
                
        return ans
        
"""
給定一個長度為 n 的 1 索引整數數組 nums。
如果 i 除以 n，即 n % i == 0，則 nums 的元素 nums[i] 被稱為特殊元素。
返回 nums 的所有特殊元素的平方和。
"""