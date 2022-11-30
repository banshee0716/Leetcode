class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr).keys())==len(set(Counter(arr).values()))