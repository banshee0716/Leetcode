from typing import List
from heapq import heappush, heappop

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 使用最大堆來存儲成績的負值和索引
        maxHeap = []
        for i, s in enumerate(score):
            heappush(maxHeap, (-s, i))
        
        # 初始化結果列表
        res = [0] * len(score)
        place = 1  # 排名計數
        
        # 處理堆中的每個元素
        while maxHeap:
            pos = heappop(maxHeap)[1]  # 獲取成績的原始索引
            if place > 3:
                rank = str(place)
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"
            
            res[pos] = rank
            place += 1
            
        return res

    """
解題思路
1. 使用最大堆：通過一個最大堆（在Python中通過存儲負值來實現）來維持成績的排序，以便能按成績從高到低處理每個運動員。
2. 遍歷成績：對每個成績和它的索引進行遍歷，將成績（存為負數）和索引一起推入堆中。
3. 分配排名：按照成績從高到低的順序，從堆中取出元素並分配相應的排名。
4. 特殊處理前三名：根據排名位置，前三名分別分配特殊的獎牌，其餘則分配數字排名。

時間複雜度分析
時間複雜度：O(n log n)，其中n是成績列表的長度。將所有成績推入堆中和從堆中取出成績都需要O(log n)時間，且這些操作對每個成績都執行一次。

空間複雜度分析
空間複雜度：O(n)，用於存儲最大堆和結果列表。
    """