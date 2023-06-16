class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 計算需要移除的左括號和右括號的數量
        redundant_open = 0
        redundat_close = 0
        for i in s:
            if i == "(":
                redundant_open += 1
            elif i == ")":
                if redundant_open > 0:
                    redundant_open -= 1
                else:
                    # 如果沒有配對的左括號，則此右括號需要被移除
                    redundat_close += 1
        
        ans = set()  # 用來儲存所有可能的有效括號字符串
        
        def dfs(index, left, right, ope, close, valid):
            # 如果遍歷到字符串結尾，檢查當前的字符串是否為有效的括號字符串
            if index == len(s):
                if left == right and ope == 0 and close == 0:
                    ans.add(valid)
                return
            
            # 對於每一個字符，都做出選擇：留下還是移除
            if s[index] == '(':
                if ope > 0:
                    dfs(index + 1, left, right, ope - 1, close, valid)  # 移除此左括號
                dfs(index + 1, left + 1, right, ope, close, valid + "(")  # 留下此左括號
            elif s[index] == ')':
                if close > 0:
                    dfs(index + 1, left, right, ope, close - 1, valid)  # 移除此右括號
                if right < left:
                    dfs(index + 1, left, right + 1, ope, close, valid + ")")  # 留下此右括號
            else:
                dfs(index + 1, left, right, ope, close, valid + s[index])  # 非括號字符，直接留下
                
        dfs(0, 0, 0, redundant_open, redundat_close, "")
        return list(ans)
"""

時間複雜度為
O(n*2^n)，因為在最壞的情況下，我們可能需要探索輸入字符串的所有子字符串。其中，n為字符串的長度。

空間複雜度為
O(n)，主要是因為深度優先搜尋的遞迴調用棧和儲存最終結果的列表。
"""