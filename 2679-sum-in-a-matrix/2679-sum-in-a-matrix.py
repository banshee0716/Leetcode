import numpy as np
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        for i in nums:
            i.sort()
        arr = np.array(nums)
        x = np.amax(arr,axis= 0)
        return sum(x)