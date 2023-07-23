class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # 遍歷字串中的每個字元
        for ch in word:
            # 如果該字元不是數字，則將其替換為空格
            if not ch.isdigit():
                word = word.replace(ch, ' ')
        
        # 利用 split 函數將字串分割成由數字構成的子字串的列表
        word = word.split()
        # 利用 set 函數將字串中的整數轉換為數字，並自動去除重複的數字
        word = set(int(i) for i in word)
        # 返回 set 的長度，即為字串中不同整數的個數
        return len(word)

"""
時間複雜度，
該程式碼的運行時間主要消耗在遍歷整個字串並替換非數字字符，其次是在 set 操作上。因此，時間複雜度為 O(n)，其中 n 是輸入字串的長度。

在空間複雜度，
我們需要儲存字串 split 後產生的列表以及 set。因此，空間複雜度也為 O(n)，其中 n 是輸入字串的長度。
"""