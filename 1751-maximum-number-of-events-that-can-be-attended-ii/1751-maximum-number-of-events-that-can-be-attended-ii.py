import bisect
from functools import cache

class Solution:
    def __init__(self):
        self.events = []

    @cache
    def solve(self, i, k):
        # 終止條件：當事件都處理完或已選擇的事件數量已達上限時，返回0
        if i >= len(self.events) or k <= 0: 
            return 0
        
        # 取出當前事件的起始時間，結束時間和價值
        s, e, v = self.events[i]
        
        # 使用二分搜尋找出下一個在當前事件結束後開始的事件
        j = bisect.bisect(self.events, [e+1])
        
        # 我們有兩種選擇：選擇當前事件或不選擇當前事件
        return max(
            v + self.solve(j, k - 1),  # 選擇當前事件
            self.solve(i + 1, k)        # 不選擇當前事件
        )

    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 先將事件根據其開始時間進行排序
        events.sort()
        self.events = events
        # 調用 solve 函式進行求解
        return self.solve(0, k)

""" 
1. 對於每一個事件，我們有兩種選擇：我們可以選擇這個事件，也可以選擇跳過這個事件。我們使用遞迴和動態規劃的方法去找出這兩種選擇中最好的一種。
2. 如果我們選擇了當前的事件，我們需要找出下一個在當前事件結束後開始的事件，我們可以使用二分搜尋的方式去找這個事件，然後遞迴調用solve函式對剩下的事件和剩下的選擇數量進行求解。
3. 如果我們選擇跳過當前的事件，我們可以直接遞迴調用solve函式對剩下的事件和剩下的選擇數量進行求解。

1. 時間複雜度是O(n log n)，其中n是事件的數量。排序事件需要O(n log n)的時間，對每個事件進行二分搜尋需要O(log n)的時間，因此總的時間複雜度是O(n log n)。

2. 空間複雜度是O(n)，其中n是事件的數量。我們需要一個數組來保存事件，並且在進行遞迴調用時，需要使用到系統的堆疊空間。
"""