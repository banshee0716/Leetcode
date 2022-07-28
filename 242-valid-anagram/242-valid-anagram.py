class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        record = [0] * 26  #哈希表
        
        for i in range(len(s)):
            record[ord(s[i])-ord("a")] += 1 #將對應的值+1
            
        for i in range(len(t)):
            record[ord(t[i])-ord("a")] -= 1 #將對應的值-1
            
        for i in range(26):
            if record[i] != 0:
                return False
            
        return True
        