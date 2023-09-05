from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 初始化答案和前綴和
        res, prefix = 0, 0
        
        # 初始化餘數的頻率哈希表，並先設定餘數為0的頻率為1
        remainderFq = defaultdict(int)
        remainderFq[0] = 1

        # 遍歷每個數字
        for n in nums:
            # 計算前綴和
            prefix += n
            
            # 計算前綴和的餘數
            remainder = prefix % k
            
            # 將該餘數出現次數累加到答案中
            res += remainderFq[remainder]
            
            # 更新該餘數的頻率
            remainderFq[remainder] += 1

        # 返回答案
        return res
    
    
"""
計算給定陣列 nums 中，有多少子陣列的和能夠被 k 整除。


前綴和 (Prefix Sum)：這個策略用於計算 nums 中每一子陣列的總和。我們可以在 O(1) 的時間內得到任何子陣列的和，只要我們知道它的開始和結束索引。

模數餘數 (Remainder)：如果兩個數的模數餘數相同，那麼這兩個數的差能夠被 k 整除。我們利用這個性質，記錄每一個模數餘數出現的次數。


時間複雜度: O(n)，其中 n 是 nums 的長度，因為我們僅遍歷整個數組一次。
空間複雜度: O(k)，其中 k 是給定的整數。在最壞情況下，哈希表會存儲 k 個不同的餘數。
"""