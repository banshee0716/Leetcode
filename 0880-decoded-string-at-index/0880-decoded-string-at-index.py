class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0  # 追踪解碼字串的長度
        
        # 前向迭代以計算解碼字串的長度
        i = 0
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])  # 使用該數字更新長度
            else:
                length += 1  # 字母使長度加 1
            i += 1
        
        # 反向迭代找到第 k 個字元
        for j in range(i-1, -1 , -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1

"""
解題思路：反向迭代
1. 初始化：先將 length 初始化為 0。這個變數會用來追踪當前解碼字串的長度。

2. 前向迭代：
    從字串的開始到結尾遍歷。
    如果遇到數字，則將 length 乘以該數字（因為它表示解碼的重複次數）。
    如果遇到字母，則 length 加 1。
    
3. 反向迭代：
    從字串的末尾開始。
    如果遇到數字，那麼將 length 除以該數字，並使用模運算更新 k。
    如果遇到字母，且 k 為 0 或等於 length，則返回該字母。

時間複雜度：O(n)，其中 n 是字串 s 的長度。因為解決方案涉及對字串的兩次遍歷。
空間複雜度：O(1)。此解決方案沒有使用與輸入大小成比例的任何附加數據結構。
"""