#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 初始化一個最小堆
        heap = []

        # 遍歷 points 中的每個點
        for (x, y) in points:
            # 計算每個點到原點的距離的平方，我們使用負數表示以便在最小堆中進行比較
            distance = -(x**2 + y**2)

            # 如果堆的大小小於 k，則將當前點加入堆中
            if len(heap) < k:
                heapq.heappush(heap, (distance, x, y))
            # 否則，將當前點和堆中的最小距離的點進行比較
            # 如果當前點距離更小，則將其替換為堆中的最小距離點
            else:
                heapq.heappushpop(heap, (distance, x, y))

        # 從堆中提取結果並返回
        return [(x, y) for (distance, x, y) in heap]


"""
時間複雜度分析：

遍歷 points 列表的時間複雜度為 O(n)，其中 n 為 points 的長度。
將 n 個點加入堆的時間複雜度為 O(nlogk)，其中 k 為需要找到的最近點的數量。
綜合以上分析，此算法的總時間複雜度為 O(n + nlogk) = O(nlogk)。

空間複雜度分析：

最小堆 heap 的空間複雜度為 O(k)。
最後返回的結果列表空間複雜度為 O(k)。
綜合以上分析，此算法的總空間複雜度為 O(k + k) = O(2k) = O(k)。
"""

# @lc code=end
