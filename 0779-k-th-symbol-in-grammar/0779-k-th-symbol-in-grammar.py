class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 終止條件：當只有一行時，返回0
        if n == 1:
            return 0
        
        # 計算當前行的長度的一半
        length = 2 ** (n - 2)
        
        # 判斷k在當前行的前半部分還是後半部分
        if k <= length:
            # 如果在前半部分，則在上一行找第k個字符
            return self.kthGrammar(n - 1, k)
        else:
            # 如果在後半部分，則在上一行找第k - length個字符，並將結果取反
            return 1 - self.kthGrammar(n - 1, k - length)


    
    """
「在第一行我們寫上一個0。接下來的每一行，將前一行的0替換為01，1替換為10。給定行數N和序列數K，返回第N行中第K個字符。（K是從1開始的）」

這個問題可以通過觀察規律和遞歸來解決。我們可以觀察到，每一行的前半部分都是上一行的內容，後半部分是上一行內容的反轉並將0換成1，1換成0。

解題思路：

終止條件：當n == 1時，序列只有一個0，直接返回0。
計算當前行的長度的一半，length = 2^(n-2)。
判斷k是否在當前行的前半部分。
如果在前半部分，則直接在上一行找第k個字符。
如果在後半部分，則在上一行找第k - length個字符，並將結果取反。

時間複雜度分析：
每進行一次遞歸，n都會減1，最多進行n次遞歸，所以時間複雜度為O(n)。

空間複雜度分析：
因為是遞歸調用，最多有n層遞歸，所以空間複雜度為O(n)。
    """