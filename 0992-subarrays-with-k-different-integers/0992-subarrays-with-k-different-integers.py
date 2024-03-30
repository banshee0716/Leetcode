class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)
    
    def subarraysWithAtMostKDistinct(self, nums, k):
        ans = 0 
        count = [0] * (len(nums) + 1)

        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                k -= 1
            while k == -1:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            ans += r - l + 1
        return ans
        
        
        
    
    """
給定一個整數數組 nums 和一個整數 k，傳回 nums 的好子數組的數量。

一個好的數組是一個數組，其中不同整數的數量正好是 k。

例如，[1,2,3,1,2] 有 3 個不同的整數：1、2 和 3。子數組是數組的連續部分。
    """