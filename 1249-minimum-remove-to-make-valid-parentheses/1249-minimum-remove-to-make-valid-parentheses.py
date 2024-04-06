class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = list(s)

        for i, char in enumerate(s):
            if char == '(': stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(': stack.pop()
                else: stack.append(i)

        for i in range(len(stack)): 
            ans[stack[i]] = ''

        return ''.join(ans)
    
    """
給定一個由 '(' , ')' 和小寫英文字元組成的字串 s。

您的任務是刪除最少數量的括號（任何位置的“(”或“)”），以便產生的括號字串有效並傳回任何有效字串。

形式上，括號字串有效當且僅當：

它是空字串，僅包含小寫字符，或者
它可以寫為 AB（A 與 B 連接），其中 A 和 B 是有效字串，或者
它可以寫成(A)，其中A是一個有效的字串。
    """