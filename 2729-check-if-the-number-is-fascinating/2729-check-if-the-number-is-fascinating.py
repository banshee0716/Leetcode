class Solution:
    def isFascinating(self, n: int) -> bool:
        def fesible(num):
            if sorted(list(n)) == ["1","2","3","4","5","6","7","8","9"]:
                return True
            else:
                return False
            
        n = str(n) + str(2*n) + str(3*n)
        return fesible(n)
    
"""
給定一個由 3 位數字組成的整數 n。

如果經過以下修改後，結果數字包含從 1 到 9 的所有數字恰好一次且不包含任何 0，我們稱數字 n 為令人著迷的數字：

將 n 與數字 2 * n 和 3 * n 連接。
如果 n 很有趣，則返回 true，否則返回 false。

連接兩個數字意味著將它們連接在一起。例如，121和371串聯爲121371。
"""