class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        res = c = 0
        d = 1 << 30
        for a in nums:
            res += max(a, b:= a ^ k)
            c ^= a < b
            d = min(d, abs(a - b))
        return res - d * c