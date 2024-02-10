class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0 
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s)) #以i為中心擴充
            result += self.extend(s, i, i+1, len(s))
            
        return result
            
    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
            
        return res