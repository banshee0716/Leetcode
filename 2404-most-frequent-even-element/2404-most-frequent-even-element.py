class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(x for x in nums if x&1 == 0)
        return min(freq, key=lambda x: (-freq[x], x), default=-1)