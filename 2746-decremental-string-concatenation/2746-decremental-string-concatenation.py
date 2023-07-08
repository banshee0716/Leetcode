from typing import List
from functools import lru_cache

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @lru_cache(None)
        def f(first: str, last: str, index: int) -> int:
            # base case: 如果 index 超出單詞的數量，返回 0
            if len(words) - 1 < index:
                return 0
            
            # 取出當前的單詞
            w = words[index]
            
            # 計算將 w 放在第一個單詞的後面和最後一個單詞的後面，兩種情況能夠節省的字母數量
            return max(
                (w[-1] == first) + f(w[0], last, index + 1),
                (last == w[0]) + f(first, w[-1], index + 1),
            )
        
        # 計算答案
        return len(''.join(words)) - f(words[0][0], words[0][-1], 1)

"""
時間複雜度為 O(n^2)，其中 n 是單詞的數量。這是因為我們需要考慮將每個單詞放在第一個位置和最後一個位置的情況，並對每種情況進行遞歸搜索。

空間複雜度為 O(n)，這主要是由於遞歸調用的深度和存儲 memoization 資訊所需的空間。
"""