class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        max_len = 0
        current_len = 0
        for num in nums:
            if num == k:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
                
        return max_len

    
"""
你有一個大小為 n 的整數數組 nums。

考慮 nums 中一個非空的子數組，其具有最大可能的按位與 (bitwise AND)。

換句話說，設 k 為 nums 中任意子數組的按位與的最大值。那麼，只考慮按位與等於 k 的子數組。 返回此類子數組中最長的長度。

數組的''按位與''是數組中所有數字的''按位與''操作結果。

子數組是數組中的一個連續元素序列。
"""