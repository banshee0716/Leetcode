class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stk = count = 0
        for c in s:
            if c == '(':
                stk += 1
            elif stk > 0:
                stk -= 1    
            else:
                count += 1
        return stk + count