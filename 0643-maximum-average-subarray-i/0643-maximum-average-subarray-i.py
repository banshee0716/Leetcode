class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
            
        return maxSum / k
        
        
        
        
        """
給定一個由 n 個元素組成的整數陣列 nums 和一個整數 k。
找到一個長度等於 k 且平均值最大的連續子數組並傳回該值。任何計算誤差小於 10-5 的答案都將被接受。
        """