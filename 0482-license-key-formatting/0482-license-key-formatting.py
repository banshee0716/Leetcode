class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 將 "-" 符號從字串中移除
        s = s.replace("-", "")

        # 計算首組的字符數量
        head = len(s) % k
        grouping = []

        # 如果首組有字符，將其添加到 grouping
        if head:
            grouping.append(s[:head])

        # 從首組之後的字符開始，每 k 個字符為一組，並添加到 grouping
        for index in range(head, len(s), k):
            grouping.append(s[index : index + k])

        # 將 grouping 中的每一組用 "-" 連接起來，並轉換為大寫
        return "-".join(grouping).upper()

        
        
"""

#我們想重新格式化字符串 s，使每個組恰好包含 k 個字符，但第一組除外，它可能比 k 短，但仍必須至少包含一個字符。
#此外，兩組之間必須插入一個破折號，並且您應該將所有小寫字母轉換為大寫字母。

時間複雜度為 O(n)，其中 n 為輸入字串的長度。因為我們需要遍歷輸入字串的每一個字符。
空間複雜度也是 O(n)。在最壞的情況下，我們需要儲存輸入字串的所有字符和中間結果。
"""