class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        @cache
        def f(i):
            return f(parent[i]) ^ (1 << (ord(s[i]) - ord('a'))) if i else 0

        count = Counter()
        res = 0
        for i in range(len(parent)):
            v = f(i)
            res += count[v] + sum(count[v ^ (1 << j)] for j in range(26))
            count[v] += 1
        return res