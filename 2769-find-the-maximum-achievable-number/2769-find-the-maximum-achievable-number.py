class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
    
"""
1. 給定兩個整數：num 和 t。
2. 如果在應用以下操作不超過 t 次後，整數 x 可以等於 num，則稱該整數 x 是可實現的：
3. 將 x 增加或減少 1，同時將 num 增加或減少 1。

返回可能達到的最大數量。可以證明至少存在一個可達到的數。

不用特別說吧，這題很明顯最大值就是每次都是x+1和num+1，重複ｔ次
"""