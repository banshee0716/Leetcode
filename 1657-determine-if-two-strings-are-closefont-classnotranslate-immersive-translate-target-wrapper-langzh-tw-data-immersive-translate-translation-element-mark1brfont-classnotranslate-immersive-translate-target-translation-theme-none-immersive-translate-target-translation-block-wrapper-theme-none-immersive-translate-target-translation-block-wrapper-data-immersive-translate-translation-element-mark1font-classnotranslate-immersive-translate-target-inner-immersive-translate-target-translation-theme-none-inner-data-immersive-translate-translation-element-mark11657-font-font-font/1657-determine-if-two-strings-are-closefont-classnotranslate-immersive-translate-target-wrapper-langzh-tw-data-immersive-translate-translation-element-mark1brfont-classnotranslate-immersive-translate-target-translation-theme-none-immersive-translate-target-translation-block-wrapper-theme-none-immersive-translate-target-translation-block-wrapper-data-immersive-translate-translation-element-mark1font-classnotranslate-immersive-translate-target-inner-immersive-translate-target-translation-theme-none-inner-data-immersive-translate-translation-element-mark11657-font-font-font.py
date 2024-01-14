class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26  # word1的字符頻率
        freq2 = [0] * 26  # word2的字符頻率

        # 計算word1的字符頻率
        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        # 計算word2的字符頻率
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # 檢查字符存在性
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        # 比較頻率
        freq1.sort()
        freq2.sort()
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True  # 兩字符串相似

"""
解題思路

1. 計算字符頻率：
    -使用兩個長度為26的數組 freq1 和 freq2 分別存儲 word1 和 word2 中每個字母的出現頻率。

2. 檢查字符存在性：
    -檢查兩個字符串中是否有字符在一個字符串中出現但在另一個中沒有。如果存在這樣的字符，則兩個字符串不相似，返回 False。

3. 比較頻率：
    -對兩個頻率數組進行排序，然後比較它們是否完全相同。如果相同，則兩個字符串相似；否則，不相似。
    
時間複雜度
    -計算字符頻率的時間複雜度為 O(n)，其中 n 為 word1 和 word2 中較長字符串的長度。
    -排序的時間複雜度為 O(26log26)，即 O(1)，因為數組長度固定為26。
    -總的時間複雜度為 O(n)。

空間複雜度
    -使用了固定大小的額外空間來存儲字符頻率，空間複雜度為 O(1)。
"""