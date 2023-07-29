class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans, cnt = 0, 0
        for i, num in enumerate(nums):
            if num > threshold:
                cnt = 0

            elif cnt and parity != num%2:
                parity^= 1
                cnt+= 1

            else:
                parity = num%2
                cnt = parity^1

            ans = max(ans, cnt)

        return ans
        
        
"""
給定一個 0 索引的整數數組 nums 和一個整數閾值。

查找從索引 l 開始到索引 r 結束的最長 nums 子數組的長度 (0 <= l <= r < nums.length)，滿足以下條件：

    nums[l] % 2 == 0
    對於 [l, r - 1] 範圍內的所有索引 i，nums[i] % 2 != nums[i + 1] % 2
    對於 [l, r] 範圍內的所有索引 i，nums[i] <= threshold
    
返回一個整數，表示最長的此類子數組的長度。

注意：子數組是數組中連續的非空元素序列。
"""