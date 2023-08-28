class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        lo, hi = 0, len(nums)-1
        pair = 0
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                pair += hi - lo
                lo += 1
            else:
                hi -= 1
                
        return pair
        
        """
        給定長度為 n 的 0 索引整數數組 nums 和整數目標，返回 (i, j) 對的數量，其中 0 <= i < j < n 且 nums[i] + nums[j] < target。
        """