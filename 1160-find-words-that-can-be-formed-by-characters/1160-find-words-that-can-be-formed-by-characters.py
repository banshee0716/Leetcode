from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 輔助函數：檢查單詞是否可以由chars構成
        def can_form(word, chars):
            char_count = Counter(chars)
            for char in word:
                if char_count[char] <= 0:
                    return False
                char_count[char] -= 1
            return True
        
        result = 0
        # 遍歷單詞，並累加可以構成的單詞的長度
        for word in words:
            if can_form(word, chars):
                result += len(word)
                
        return result


        
        
    
    """
給你一個字串單字數組和一個字串字元數組。

如果字串可以由 chars 中的字元組成（每個字元只能使用一次），則該字串很好。

傳回所有好的字串的長度總和（以單字為單位）。

总体时间复杂度为 O(n + m * k)。

使用了额外的空间来存储字符计数，空间复杂度为 O(1)，因为字符集的大小是固定的（最多 26 个英文字母）。
    """