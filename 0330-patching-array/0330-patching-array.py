class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            
            else:
                miss += miss
                result += 1
                
        return result
        

    
    """
給定一個排序的整數數組 nums 和一個整數 n，向數組添加/修補元素，以便 [1, n] 範圍內的任何數字都可以由數組中某些元素的總和形成。

傳回所需的最小補丁數。
    """