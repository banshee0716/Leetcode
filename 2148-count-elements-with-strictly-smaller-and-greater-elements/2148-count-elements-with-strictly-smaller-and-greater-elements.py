class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        
        return sum(1 for i in nums if min_num < i < max_num)
        
        
        """
        給定一個整數數組 nums，返回 nums 中同時出現嚴格較小和嚴格較大元素的元素數量。
        """