from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 對硬幣堆進行排序
        piles.sort()
        res = 0
        # 從後向前選取硬幣，每次跳過一堆
        for i in range(len(piles) // 3, len(piles), 2):
            res += piles[i]
            
        return res

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準

        
        
        
    """
解題思路：

1. 排序：
    -首先對硬幣堆進行排序，使得我們可以從後向前選取硬幣堆。
    
2. 選取硬幣：
    -從後向前選取硬幣堆，每次跳過一堆（即選取間隔為2的硬幣堆）。選取的起始點是從總堆數的三分之一處開始（因為每次要丟棄一大一小兩堆，所以每三堆中只有一堆是有效的）。
    
3.計算結果：
    -將選取的硬幣數量加起來，得到最終結果。
    
時間複雜度
為 O(n log n)。

空間複雜度分析：
除了給定的硬幣堆列表之外，只使用了一個變量來儲存結果，因此空間複雜度為 O(1)。
    """