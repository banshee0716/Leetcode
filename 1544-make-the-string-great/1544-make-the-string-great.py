class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and abs(ord(stack[-1]) - ord(i)) == 32:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
            
        
    #把鄰近的一個小寫跟大寫刪除，只留下單純的