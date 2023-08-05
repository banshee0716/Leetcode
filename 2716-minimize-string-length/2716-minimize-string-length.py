class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
    
"""
給定一個索引為 0 的字符串 s，重複執行以下操作任意次：

在字符串中選擇一個索引 i，並令 c 為位置 i 的字符。刪除最接近 i 左側出現的 c（如果有）以及最接近 i 右側出現的 c（如果有）。
您的任務是通過多次執行上述操作來最小化 s 的長度。

返回一個整數，表示最小化字符串的長度。
"""