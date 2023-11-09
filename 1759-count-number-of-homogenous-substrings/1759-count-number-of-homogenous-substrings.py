class Solution:
    def countHomogenous(self, s: str) -> int:
        
        res, count, n = 0, 1, len(s)
        for i in range(1,n):
            if s[i] == s[i-1]:
                count+=1
            else:
                if count>1:
                    res+=(count*(count-1)//2)
                count=1  
                
        if count>1:
            res+=(count*(count-1)//2)
            
        return (res+n)%(10**9+7)
    
    
    
        """
        給定一個字串 s，傳回 s 的同質子字串的數量。由於答案可能太大，因此傳回 109 + 7 求模的結果。

如果字串中的所有字元都相同，則該字串是同質的。

子字串是字串中連續的字元序列。
        """