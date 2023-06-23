class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, cur = 0, 0
        for i in nums:
            if i == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
                
        return ans