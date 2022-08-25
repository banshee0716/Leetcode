class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr =[0]*26
        for i in magazine:
            arr[ord(i)-ord('a')] +=1
            
        for i in ransomNote:
            if arr[ord(i)-ord('a')] == 0:
                return False
            else:
                arr[ord(i)-ord('a')] -= 1
                
        return True