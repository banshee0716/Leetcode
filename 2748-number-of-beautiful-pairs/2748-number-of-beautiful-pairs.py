class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i, num in enumerate(nums):
            d = num % 10
            for j in range(i):
                
                n = nums[j]
                while n >= 10:
                    n //= 10
                pairs += gcd(d, n) == 1
        
        return pairs

"""
給定一個 0 索引的整數數組 nums。如果 nums[i] 的第一個數字和 nums[j] 的最後一個數字互質，
則一對索引 i, j（其中 0 <= i < j < nums.length）被稱為美麗的。

返回美麗對的總數（以 nums 為單位）。

如果沒有大於 1 的整數可以整除兩個整數 x 和 y，則這兩個整數 x 和 y 互質。
換句話說，如果 gcd(x, y) == 1，則 x 和 y 互質，其中 gcd(x, y) 是 x 和 y 的最大公約數。
"""