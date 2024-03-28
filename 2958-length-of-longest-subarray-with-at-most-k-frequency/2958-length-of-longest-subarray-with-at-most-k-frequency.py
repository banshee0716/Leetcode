class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        l = 0
        n = len(nums)
        
        for r in range(n):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if mp[nums[r]] > k:
                while nums[l] != nums[r]:
                    mp[nums[l]] -= 1
                    l += 1
                    
                mp[nums[l]] -= 1
                l += 1
            
            ans = max(r-l+1, ans)
            
        return ans
                
                
        
        
        
        
        """
給定一個整數數組 nums 和一個整數 k。元素 x 的頻率是它在陣列中出現的次數。

如果數組中每個元素的頻率小於或等於 k，則該數組稱為良好數組。

傳回 nums 的最長有效子數組的長度。子數組是數組中連續的非空元素序列。
        """