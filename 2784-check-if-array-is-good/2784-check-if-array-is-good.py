class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        return Counter(nums) == Counter(range(1,n)) + Counter((n-1,))
        
        
        
"""
給定一個整數數組 nums。如果一個數組是數組 base[n] 的排列，我們就認為它是好的。

base[n] = [1, 2, ..., n - 1, n, n] （換句話說，它是一個長度為 n + 1 的數組，其中僅包含一次 1 到 n - 1，加上兩次出現的 n）。例如，基[1] = [1, 1] 和基[3] = [1, 2, 3, 3]。

如果給定的數組是好的，則返回 true，否則返回 false。

注意：整數的排列表示這些數字的排列。

1. 確定array在sort之後是不是有符合是(1, n)+n的狀態
2. 可以計算一下數字是不是有吻合就好
"""