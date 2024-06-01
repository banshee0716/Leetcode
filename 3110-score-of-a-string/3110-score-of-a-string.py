class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i]) - ord(s[i+1]))
            
        return score
        
    
    """
給你一個字串 s。字串的分數定義為相鄰字元的 ASCII 值之間的絕對差之和。

傳回 s 的分數。
    """