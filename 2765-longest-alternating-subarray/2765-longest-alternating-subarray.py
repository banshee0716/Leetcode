class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
        res = -1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                longest = 2
                for j in range(i + 2, len(nums)):
                    if j < len(nums) and nums[j] == nums[j - 2]:
                        longest += 1
                    else:
                        break
                res = max(res, longest)
        return res if res != 0 else -1

