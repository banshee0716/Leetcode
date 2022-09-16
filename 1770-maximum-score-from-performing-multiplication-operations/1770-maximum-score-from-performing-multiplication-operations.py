class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        
        @lru_cache(2000)
        def dp(l, i):
            if i == m: return 0
            pickLeft = dp(l+1, i+1) + nums[l] * multipliers[i] # Pick the left side
            pickRight = dp(l, i+1) + nums[n-(i-l)-1] * multipliers[i] # Pick the right side
            return max(pickLeft, pickRight)
        
        return dp(0, 0)