import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # 最小堆
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:  # 如果最小堆的大小超過了梯子數量
                    bricks -= heapq.heappop(heap)  # 使用磚塊
                if bricks < 0:  # 如果磚塊不足
                    return i  # 返回當前索引
        
        return len(heights) - 1  # 如果能夠走完整個數組

                
"""
這題的核心思想是利用優先隊列（最小堆）來決定哪些高度差應該用梯子跨過，哪些應該用磚塊。

1. 遍歷高度差：
    -遍歷heights數組，計算每對相鄰建築之間的高度差diff。
    -如果diff大於0（表示需要上升），則將diff加入到最小堆heap中。

2. 使用梯子和磚塊：
    -如果最小堆的大小超過了梯子的數量，表示不能對所有的上升使用梯子，此時應該從堆中彈出最小的高度差，使用磚塊來跨過。
    -從bricks中扣除最小堆頂部的高度差。
    -如果磚塊數量bricks變成負數，表示無法使用磚塊跨過當前的高度差，因此返回當前索引i作為最遠到達的建築。

3. 返回結果：
    -如果能夠走完整個數組，則返回len(heights) - 1作為最遠到達的建築索引。
    
時間複雜度
    -遍歷數組的時間複雜度為O(N)，其中N是heights數組的長度。
    -每次遍歷時，可能進行一次堆操作，堆操作的時間複雜度為O(logK)，其中K是梯子數量。
    -因此，總的時間複雜度為O(NlogK)。

空間複雜度
    -最小堆heap的空間複雜度為O(K)，其中K是梯子數量。
    -因此，總的空間複雜度為O(K)。
    
"""