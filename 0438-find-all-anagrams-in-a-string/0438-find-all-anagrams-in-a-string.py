class Solution:
    def countarr(self,w): 
        out = [0]*26
        for c in w:
            out[ord(c)-ord('a')]+=1
        return out
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        ps = self.countarr(p)
        ans = []
        ss = self.countarr(s[:m])
        
        if ss == ps:
            ans = [0]
        
        for i in range(1,len(s)-m+1):
            
            left = ord(s[i-1])-ord('a') 
            right = ord(s[i+m-1])-ord('a')
            ss[left] = ss[left] -1
            ss[right] = ss[right] +1
            
            if ss == ps:
                ans.append(i)
        return ans
        