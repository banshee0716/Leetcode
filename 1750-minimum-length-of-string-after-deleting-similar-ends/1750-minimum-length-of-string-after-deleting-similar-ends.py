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

解題思路
1. 雙指針方法：
    -使用兩個指針left和right分別指向字符串s的開頭和結尾。

2.移動指針：
    -當left < right且s[left]等於s[right]時，說明目前開頭和結尾的字符相同，需要進行刪除。
    -使用一個變量char記錄當前需要刪除的字符，然後分別從左到右和從右到左移動left和right指針，跳過所有與char相同的字符。

3. 計算剩餘長度：
    -當left指針大於等於right指針時，表示中間的字符已經是不需要再刪除的部分，或者字符串已經被刪除完畢。
    -此時，返回right - left + 1作為剩餘字符串的長度。
    
時間複雜度
    -遍歷字符串的時間複雜度為O(N)，其中N是字符串s的長度。在最壞的情況下，我們可能需要從兩端向中心遍歷整個字符串。

空間複雜度
    -本算法只使用了固定的額外空間（即幾個指針和變量），因此空間複雜度為O(1)。
    """