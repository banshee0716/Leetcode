class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0 
        for x in range(low, high+1): 
            s = str(x)
            if not len(s) & 1: 
                bal = 0 
                for i, ch in enumerate(s): 
                    if i < len(s)//2: bal += int(ch)
                    else: bal -= int(ch)
                if bal == 0: ans += 1
        return ans 