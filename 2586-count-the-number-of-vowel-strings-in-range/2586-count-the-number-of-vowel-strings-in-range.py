from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # 定義所有元音字母的集合
        vowels = "aeiouAEIOU"
        
        # 初始化計數器
        count = 0
        
        # 遍歷索引範圍 [left, right] 內的所有字串
        for i in range(left, right + 1):
            # 檢查字串的開頭和結尾是否都是元音字母
            if words[i][0] in vowels and words[i][-1] in vowels:
                # 若是，則計數器加 1
                count += 1
                
        # 返回計數器的值
        return count

        
"""
解題思路
1. 定義一個集合 vowels 來存放所有的元音字母（包括大寫和小寫，雖然題目沒有明確說明大小寫）。
2. 初始化一個計數器 count 為0。
3. 遍歷字串陣列 words 中索引從 left 到 right 的所有元素。
4. 檢查每個字串的第一個字元和最後一個字元是否都在 vowels 集合中。
    - 如果是，則 count 加1。
5. 返回 count。

時間複雜度: 我們僅遍歷了索引範圍 [left, right] 的字串，每次檢查第一個和最後一個字元是否為元音字母。時間複雜度是 O(n)，
其中 n=right−left+1。

空間複雜度: 我們只使用了常數空間，所以空間複雜度是 O(1)。

"""