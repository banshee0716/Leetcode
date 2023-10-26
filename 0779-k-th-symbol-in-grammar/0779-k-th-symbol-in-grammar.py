class Solution:
    
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: 
            return 0
        half = 2**(N - 2) 
        
        if K > half:
            return 1 if self.kthGrammar(N - 1, K - half) == 0 else 0
        else:
            return self.kthGrammar(N - 1, K)
    
    """
我們建立一個包含 n 行的表（1 索引）。我們先在第一行寫入 0。現在，在每個後續行中，我們查看前一行，並將每次出現的 0 替換為 01，每次出現的 1 替換為 10。

例如，對於 n = 3，第一行是 0，第二行是 01，第三行是 0110。
給定兩個整數 n 和 k，傳回 n 行表的第 n 行中的第 k 個（1 索引）符號。
    """