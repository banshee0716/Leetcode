class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
                
            else:
                mp[sum_val] = i
        
        return max_len
                
        
        
        
        #給定一個二進制數組 nums，傳回具有相同數量的 0 和 1 的連續子數組的最大長度。
        