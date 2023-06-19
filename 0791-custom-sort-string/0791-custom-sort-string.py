class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = ""  # 儲存結果的字串
        mapping = {}  # 儲存字串 s 中每個字符的計數

        # 遍歷字串 s 中的每個字符
        for sym in s:
            # 對每個字符進行計數
            mapping[sym] = mapping.get(sym, 0) + 1

        # 遍歷字串 order 中的每個字符
        for sym in order:
            # 如果字符在 mapping 中
            if sym in mapping:
                # 將字符附加到結果字串中，並將其出現的次數附加到結果字串中
                answer += sym * mapping[sym]
                # 從 mapping 中刪除該字符
                mapping.pop(sym)

        # 將未在 order 中的字符附加到結果字串的末尾
        for sym in mapping.keys():
            answer += sym * mapping.get(sym, 0)

        return answer  # 返回結果字串

"""
首先對字串 s 中的所有字符進行計數，然後根據字串 order 中的字符順序來組合結果字串。最後將未在 order 中的字符附加到結果字串的末尾。

時間複雜度為 O(n + m)，其中 n 是字串 s 的長度，m 是字串 order 的長度。因為我們需要遍歷這兩個字串。
空間複雜度為 O(n)，其中 n 是字串 s 的長度。因為我們需要建立一個映射來儲存字串 s 中的每個字符以及其對應的計數。
"""