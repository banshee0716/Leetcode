class Solution:
    def isCircularSentence(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == " " and s[i-1] != s[i+1]:
                return False
            
        return s[0] == s[-1]
        
#單詞的最後一個字符等於下一個單詞的第一個字符。
#最後一個單詞的最後一個字符等於第一個單詞的第一個字符。