class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            
            if nums[i] < nums[i-1]:
                nums = nums[i:] + nums[:i]
                return n-i if nums == sorted(nums) else -1
            
        return 0    
        
        
    """
給您一個0個索引的陣列，其中包含獨特的正整數的長度n。返回對NUMS進行排序所需的最小偏移數量，如果不可能，則返回-1。

正確的偏移定義為將索引I處的元素轉移到索引（i + 1）％n，對於所有索引。
    """