class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (1 + n) * n // 2 - (1 + n // m) * (n // m) * m