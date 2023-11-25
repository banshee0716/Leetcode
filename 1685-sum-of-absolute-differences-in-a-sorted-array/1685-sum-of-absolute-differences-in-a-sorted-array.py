class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]
        
        for i in range(n):
            current_absolute_diff = ((nums[i] * i) - prefix_sum[i]) + (suffix_sum[i] - (nums[i] * (n - i - 1)))
            result[i] = current_absolute_diff
            
        return result
            
        
    """
    給定一個按非降序排序的整數數組 nums。

建構並傳回與 nums 長度相同的整數陣列結果，使得 result[i] 等於 nums[i] 與陣列中所有其他元素之間的絕對差總和。

換句話說，result[i] 等於 sum(|nums[i]-nums[j]|)，其中 0 <= j < nums.length 且 j != i（從 0 開始索引）。
    """