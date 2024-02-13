class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.check(word):
                return word
            
        return ""
        
    def check(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return False
        
        return True
                
            
    
    """給定一個字串單字數組，傳回數組中的第一個回文字串。如果不存在這樣的字串，則傳回空字串「」。

如果一個字串向前和向後讀取相同，則該字串是回文字串。"""