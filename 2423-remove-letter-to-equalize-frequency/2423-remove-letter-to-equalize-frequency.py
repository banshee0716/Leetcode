from collections import Counter

class Solution:

    def isequal(self, c: str) -> bool:
        # 使用Counter計算c中每個字母的頻率
        c = Counter(c)
        # 判斷所有字母的頻率是否相同
        return len(set(c.values())) == 1

    def equalFrequency(self, word: str) -> bool:
        # 遍歷word的每一個字母
        for i in range(len(word)):
            # 嘗試移除第i個字母並檢查剩下的字母的頻率
            if self.isequal(word[:i] + word[i + 1:]):
                return True
        return False

    
    """
解題思路：

遍歷字串的每一個字母，嘗試移除該字母並檢查剩下的字串中的字母頻率是否都相同。
使用Counter工具來計算每個字母的頻率。
使用set確保頻率唯一，如果set的大小為1，則所有字母的頻率相同。

時間複雜度：O(n^2)，其中n是字串的長度。這是因為我們遍歷每一個字母，然後使用Counter計算其頻率，Counter的時間複雜度是O(n)。
空間複雜度：O(n)，Counter會使用O(n)的額外空間
    """