class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        romanMap ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:
            if romanMap[i] >= prev:
                res += romanMap[i]
            else:
                res -= romanMap[i]
            
            prev = romanMap[i]
        
        return res