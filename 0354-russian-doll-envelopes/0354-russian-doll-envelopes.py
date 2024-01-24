from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 按寬度升序、高度降序排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        res = []  # 存儲最長遞增子序列的高度
        for _, h in envelopes:
            idx = bisect_left(res, h)  # 二分查找適合的插入位置
            if idx == len(res):  # 如果是最大的，追加到末尾
                res.append(h)
            else:  # 否則替換掉該位置的元素
                res[idx] = h
        return len(res)  # 返回最長遞增子序列的長度

        
    
    """
解題思路
1. 排序信封：
    -首先按照寬度對信封進行升序排序。如果寬度相同，則按照高度降序排序。這樣可以確保在寬度相同的情況下，不會有兩個信封互相套娃。
2.動態規劃與二分查找：
    -創建一個新的列表 res 來存儲最長遞增子序列。對於每個信封的高度，使用二分查找在 res 中找到合適的位置插入。
3.更新 res：
    -如果找到的索引等於 res 的長度，則將當前信封的高度追加到 res。
    -如果找到的索引小於 res 的長度，則用當前信封的高度替換在該索引位置的元素。
    
時間複雜度
    -對信封排序的時間複雜度為 O(n log n)，其中 n 是信封的數量。
    -對每個信封進行二分查找並更新 res 的時間複雜度為 O(n log k)，其中 k 為 res 的長度。
    -總的時間複雜度為 O(n log n)。

空間複雜度
    -需要額外的空間來存儲排序後的信封數組和動態規劃數組 res，空間複雜度為 O(n)。
    """