from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 將工人依據工資效率比（wage/quality）進行排序
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)], key=lambda x: x[0])
        max_heap = []
        quality_sum = 0
        res = float('inf')

        # 初始化前 k 個工人到最大堆中，計算這些工人的效率值總和
        for wage_efficiency_ratio, quality in workers[:k]:
            heapq.heappush(max_heap, -quality)
            quality_sum += quality

        # 計算初始化階段的最低工資總和
        res = workers[k-1][0] * quality_sum

        # 為每一位額外的工人更新最大堆，並重新計算可能的最低工資總和
        for wage_efficiency_ratio, quality in workers[k:]:
            heapq.heappush(max_heap, -quality)
            quality_sum += quality + heapq.heappop(max_heap)
            res = min(res, wage_efficiency_ratio * quality_sum)

        return res


"""
題目描述
給定三個陣列，quality、wage 分別代表工人的工作效率和他們要求的最低工資，以及一個整數 k 表示需要雇傭的工人數量。工人的工資由他們的「效率值」決定，即某個工人的工資至少應該是他要求的最低工資和他的效率值與雇主付出的最高效率值的比例的乘積。求雇佣 k 位工人所需的最低工資總和。

解題思路
這個問題可以通過排序和最大堆（max-heap）來解決。

1. 按工資效率比排序：對每個工人計算他們的「工資/效率」比值，並按此比值升序排序。這樣可以保證當我們逐步選取工人時，總是選擇到目前為止最優秀的工人。
2. 使用最大堆維護效率：使用最大堆存儲已選取工人的效率值。堆的大小保持為 k，這樣可以快速計算出當前選取的工人的效率總和。
3. 計算最小工資：對每個工人，更新堆中的效率值，計算可能的最低工資，並持續更新最小工資。


時間複雜度：O(N log N)，因為需要對工人按照工資效率比進行排序，並且使用了堆結構來進行多次插入和刪除操作。
空間複雜度：O(N)，堆的大小最大為 N，並且還存儲了排序後的工人列表。
"""