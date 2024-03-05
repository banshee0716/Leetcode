class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1
            
        
    
    
    """
給定一個僅由字元 'a'、'b' 和 'c' 組成的字串 s。系統會要求您對字串套用以下演算法任意次：

    1.從字串 s 中選取一個非空前綴，其中前綴中的所有字元都相等。
    2.從字串 s 中選取一個非空後綴，其中該後綴中的所有字元都相等。
    3.前綴和後綴不應在任何索引處相交。
    4.前綴和後綴的字元必須相同。
    5.刪除前綴和後綴。

傳回執行上述操作任意次（可能零次）後 s 的最小長度。
    """