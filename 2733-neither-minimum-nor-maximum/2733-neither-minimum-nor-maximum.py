class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_nums, min_nums = max(nums), min(nums)
        for n in nums:
            if n != max_nums and n != min_nums:
                return n
            
        return -1
        """"""