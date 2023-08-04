class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        
        return i + n - 1 - j - (i > j)
        
"""
給定一個 n 個整數 nums 的 0 索引排列。

如果第一個數等於 1 並且最後一個數等於 n，則排列稱為半有序排列。您可以根據需要多次執行以下操作，直到使 nums 成為半有序排列：

選取 nums 中兩個相鄰的元素，然後交換它們。
返回使 nums 成為半有序排列的最小操作數。

排列是長度為 n 的從 1 到 n 的整數序列，其中每個數字恰好包含一次。
"""