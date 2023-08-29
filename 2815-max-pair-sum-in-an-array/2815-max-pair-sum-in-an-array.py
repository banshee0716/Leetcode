from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # 初始化結果為-1，以及一個預設字典來儲存每個最大位數對應的最大數字
        res, d = -1, defaultdict(int)
        
        # 遍歷每個數字
        for n in nums:
            # 找出這個數字的最大位數
            maxD = max(str(n))
            
            # 如果字典中有這個最大位數的記錄，則嘗試更新結果
            if d[maxD]: 
                res = max(res, n + d[maxD])
            
            # 更新字典中最大位數對應的最大數字
            d[maxD] = max(n, d[maxD])
        
        # 返回最終結果
        return res

        
"""
解題思路
1. 使用一個字典（d）來儲存每個最大位數對應的最大數字。
2. 遍歷列表中的每個數字，找出該數字的最大位數（maxD）。
3. 如果字典中已經有這個最大位數（maxD）的紀錄，則更新結果（res）。
4. 更新字典中最大位數對應的最大數字。

時間複雜度：O(n)，其中 n 是數字列表的長度。我們只需要遍歷一次列表。
空間複雜度：O(d)，其中 d 是不同最大位數的數量。在最壞的情況下，這個數量可能會接近10（位數從0到9）。
"""