class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxlength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else :
                maxlength = max(maxlength , i-start+1)
                
            usedChar[s[i]] = i
            
        return maxlength