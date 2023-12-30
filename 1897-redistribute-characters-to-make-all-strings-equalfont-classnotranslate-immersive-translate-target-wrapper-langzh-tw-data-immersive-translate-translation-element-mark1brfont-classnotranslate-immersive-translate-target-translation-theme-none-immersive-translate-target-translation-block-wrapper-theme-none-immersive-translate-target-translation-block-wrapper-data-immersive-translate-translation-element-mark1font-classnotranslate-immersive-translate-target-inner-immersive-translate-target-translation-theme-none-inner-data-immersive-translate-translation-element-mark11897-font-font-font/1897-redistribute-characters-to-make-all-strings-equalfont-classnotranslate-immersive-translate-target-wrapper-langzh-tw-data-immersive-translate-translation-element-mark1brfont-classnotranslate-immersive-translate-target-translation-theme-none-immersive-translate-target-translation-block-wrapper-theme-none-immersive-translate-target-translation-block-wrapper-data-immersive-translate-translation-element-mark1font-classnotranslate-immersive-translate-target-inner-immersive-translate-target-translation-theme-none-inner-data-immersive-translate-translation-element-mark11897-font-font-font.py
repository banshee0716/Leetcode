from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}  # 字符出現次數統計
        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1  # 累加字符出現次數

        n = len(words)  # 字符串數量
        for val in counts.values():  # 遍歷每個字符的出現次數
            if val % n != 0:  # 如果出現次數不能被字符串數量整除
                return False
            
        return True  # 所有字符出現次數都能被整除

"""
解題思路：

統計字符出現次數：
    使用一個字典 counts 來統計每個字符在所有字符串中出現的總次數。

檢查可行性：
    檢查每個字符的出現次數是否能被字符串數量整除。如果有任何一個字符的出現次數不能被字符串數量整除，則不可能將所有字符串重新排列使其相等。

返回結果：
    如果所有字符的出現次數都能被字符串數量整除，返回 True；否則返回 False。

時間複雜度分析：
統計字符出現次數的遍歷時間複雜度為 O(m * k)，其中 m 是 words 中字符串的數量，k 是字符串的平均長度。
檢查每個字符的出現次數是否能被整除的時間複雜度為 O(26)，因為英文字母總數為 26。在最壞情況下，每個字母都會出現。
總的時間複雜度為 O(m * k + 26)，近似為 O(m * k)。

空間複雜度分析：
需要額外的空間來存儲字符出現次數的字典，空間複雜度為 O(26)，近似為 O(1)。
"""