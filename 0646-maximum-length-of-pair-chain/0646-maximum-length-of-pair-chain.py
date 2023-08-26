from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 對所有的對按照第二個元素進行排序
        pairs.sort(key=lambda x: x[1])
        # 初始化 cur 和 ans
        cur, ans = float("-inf"), 0
        # 遍歷所有的對
        for pair in pairs:
            # 如果該對的第一個元素大於 cur
            if cur < pair[0]:
                # 更新 cur 和 ans
                cur = pair[1]
                ans += 1
        # 返回 ans
        return ans

    """
題目646要求我們找到一個最長的鏈，滿足鏈中每一個元素[a, b]和它後面的元素[c, d]滿足b < c。

解題思路，greedy　algorithm：
1. 首先對所有的對（pairs）按照第二個元素進行排序。這樣做是因為我們希望先考慮那些第二個元素比較小的對，這樣有更大的可能性能夠將它們加入到更長的鏈中。

2. 初始化一個變量cur為float('-inf')，用來存儲目前鏈中最後一個對的第二個元素。另外初始化一個變量ans為0，用來計數目前找到的最長鏈的長度。

3. 遍歷所有的對，對於每一個對，檢查它的第一個元素是否大於cur，如果是，則更新cur為該對的第二個元素，並且ans加1。

時間複雜度: 
O(n log n)，其中 n 是pairs的長度。排序需要 O(n log n) 的時間，其餘操作都是 O(n)。

空間複雜度: 
O(1)，我們只用了常數級別的額外空間。
    """
