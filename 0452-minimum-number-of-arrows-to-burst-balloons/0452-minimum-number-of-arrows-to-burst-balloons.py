from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 根據氣球的結束位置排序
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        curr_end = points[0][1]
        for xstart, xend in points:
            # 如果當前氣球的開始位置大於最近一箭的結束位置，射出新的箭
            if xstart > curr_end:
                arrows += 1
                curr_end = xend
                
        return arrows

    """
演算法思路
這是一個典型的貪婪算法問題，可以通過以下步驟求解：

排序：首先，根據每個氣球的結束位置對氣球進行排序。排序的目的是讓我們按照氣球結束位置的順序來射箭，這樣能夠最大化每一箭的效用。
遍歷並射箭：從排序後的第一個氣球開始，將箭射在當前氣球的結束位置。這保證了當前氣球被爆破，同時最大化了這一箭可能爆破的其他氣球數量。
統計箭數：如果下一個氣球的開始位置在當前箭射出的位置之後，意味著需要再射出一箭；否則，當前箭可以繼續爆破後續的氣球。每次需要射出新的箭時，箭數加一。

時間複雜度分析
排序的時間複雜度為O(NlogN)，其中N是氣球的數量。
一次遍歷的時間複雜度為O(N)。
總時間複雜度為O(NlogN)。

空間複雜度分析
這個解法只使用了常數級別的額外空間（用於存儲箭數和當前箭的結束位置），因此空間複雜度為O(1)。
    """