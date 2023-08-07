class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and stack[-1] + c in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(c)
                
        return len(stack)
    
    
    """
    
給定一個僅由大寫英文字母組成的字符串 s。

您可以對此字符串應用一些操作，其中在一次操作中，您可以從 s 中刪除子字符串“AB”或“CD”之一的任何出現。

返回可以獲得的結果字符串的最小可能長度。

請注意，刪除子字符串後字符串會連接起來，並可能產生新的“AB”或“CD”子字符串。
    """