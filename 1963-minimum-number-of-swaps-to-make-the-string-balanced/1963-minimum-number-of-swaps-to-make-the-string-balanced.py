class Solution:
    def minSwaps(self, s: str) -> int:
        
        res, bal = 0, 0
        for ch in s:
            bal += 1 if ch == '[' else -1
            if bal == -1:
                res += 1
                bal = 1
        return res
        
        
        """
給定一個長度為 n 的偶數索引 0 的字串 s。字串恰好由 n/2 個左括號「[」和 n/2 個右括號「]」組成。

當且僅當滿足以下條件時，字串才稱為平衡字串：

它是空字串，或者
它可以寫成AB，其中A和B都是平衡弦，或者
可以寫成[C]，其中C是平衡串。
您可以多次交換任兩個索引處的括號。

傳回使 s 平衡的最小交換次數。
        """