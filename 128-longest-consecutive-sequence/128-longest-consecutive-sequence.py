class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest, cur = 0, min(1, len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                cur += 1
            else :
                longest = max(longest,cur)
                cur = 1
                
        return max(longest,cur)