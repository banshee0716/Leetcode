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
1. 前綴和與模數：一個經典的方法來解決這類型的問題是使用前綴和。前綴和是指一個數字序列中從第一個數到當前數的和。使用這個和與 k 的模數，可以幫助我們快速找到子陣列的和是否能被 k 整除。

2. 餘數頻率的哈希表：在計算過程中，我們維護一個哈希表 remainderFq，它存儲每個餘數的出現次數。每次我們計算前綴和模 k 的結果，我們就查找這個餘數之前出現了多少次，然後更新答案 res。


時間複雜度: O(n)，其中 n 是 nums 的長度，因為我們僅遍歷整個數組一次。
空間複雜度: O(k)，其中 k 是給定的整數。在最壞情況下，哈希表會存儲 k 個不同的餘數。
"""