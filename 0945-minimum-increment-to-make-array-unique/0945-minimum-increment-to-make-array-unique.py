class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament
        
    
"""
給定一個整數數組 nums。在一步操作中，您可以選擇一個索引 i，其中 0 <= i < nums.length 並將 nums[i] 加 1。
傳回使 nums 中的每個值唯一的最小移動次數。
產生測試案例，以便答案適合 32 位元整數。
"""