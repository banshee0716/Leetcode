class Solution:
    def minOperations(self, s: str) -> int:
        
        start0 = 0
        start1 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        
        return min(start0, start1)

        
    
    
    """
給定一個僅由字元“0”和“1”組成的字串 s。在一次操作中，您可以將任何“0”更改為“1”，反之亦然。

如果沒有兩個相鄰字元相等，則該字串稱為交替字串。例如，字串“010”是交替的，而字串“0100”則不是。

傳回使 s 交替所需的最少操作數。


使得i-1和i+1都不等於自己
    """