class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''  # 初始化一個空字串來存儲結果
        l, r = 0, 0  # 使用l和r來標記每個單詞的開始和結束位置

        while r < len(s):  # 確保r不超出字串的長度
            if s[r] != " ":  # 如果當前字符不是空格，將r向右移動
                r += 1
            else:  # 如果找到一個空格，表明找到了一個單詞
                res += s[l:r][::-1] + " "  # 反轉這個單詞並添加到結果字串中
                r += 1  # 移動r，跳過空格
                l = r  # 將l設置為r，開始下一個單詞的搜索
        
        # 處理最後一個單詞，因為它可能不會以空格結束
        res += s[l:r][::-1]
        return res
"""
時間複雜度分析：

我們遍歷了一次輸入字串，並對其中的每個單詞進行了一次反轉操作，所以時間複雜度是O(n)，其中n是輸入字串的長度。
空間複雜度分析：

我們使用了一個額外的字串來儲存結果，所以空間複雜度是O(n)。
"""