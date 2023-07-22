class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = res = 0
        dic = {}
        for j, num in enumerate(nums):
            t = dic.copy()
            for k, v in t.items():
                if abs(k - num) > 2:
                    i = max(i, v + 1)
                    dic.pop(k)
            dic[num] = j
            res += j - i + 1
        return res
            
            
"""
給定一個 0 索引的整數數組 nums。如果滿足以下條件，則 nums 的子數組稱為連續子數組：

令 i, i + 1, ..., j 為子數組中的索引。然後，對於每對索引 i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2。

返回連續子數組的總數。子數組是數組中連續的非空元素序列。
"""