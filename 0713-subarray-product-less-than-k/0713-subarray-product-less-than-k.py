class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, right, product, count = 0, 0, 1, 0
        
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            
            count += 1 + (right-left)
            right += 1
        
        return count
            
        
        
        
        """
        給定一個整數數組 nums 和一個整數 k，傳回連續子數組的數量，其中子數組中所有元素的乘積嚴格小於 k。
        """
        