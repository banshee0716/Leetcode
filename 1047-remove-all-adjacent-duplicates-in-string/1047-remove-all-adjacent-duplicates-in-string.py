class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
        
        
        
    #運用stack，把遇到的儲存。
    #檢測現在的是不是已經有在裡面,還有是不是跟STACK[-1]相同,是的話POP掉,否則APPEND