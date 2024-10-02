class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return map(dict(zip(sorted(set(arr)), itertools.count(1))).get, arr)
