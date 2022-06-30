class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mid = sorted(nums)[len(nums) / 2]
        return sum(abs(num-mid) for num in nums)
    