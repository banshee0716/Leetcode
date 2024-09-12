class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(allowed) >= set(i) for i in words)