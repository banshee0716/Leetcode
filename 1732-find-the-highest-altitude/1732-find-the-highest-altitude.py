class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        return max([0] + list(accumulate(gain)))