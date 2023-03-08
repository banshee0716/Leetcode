'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        sum_nums = 1
        for i in range(len(nums)):
            sum_nums *= nums[i]#會溢位'''

        


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        n = len(nums)
        ans = [1]*n
        for i in range(n):
            ans[i] *= prev
            prev *= nums[i]
            
        prev = 1
        
        for i in range(n-1, -1, -1):
            ans[i] *= prev
            prev *= nums[i]
        
        return ans
            
