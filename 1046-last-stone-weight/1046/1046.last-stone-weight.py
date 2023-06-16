#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 將每個石頭重量取負值，方便用heapq建最大堆。
        # 由於heapq只支援最小堆，因此取負數使之成為最小堆。
        for i, stone in enumerate(stones):
            stones[i] = -stone
        heapq.heapify(stones)

        # 依序取出最大的兩塊石頭，做碰撞計算後放回堆中。
        # 當石頭只剩下一塊或是全部被碰撞成碎片時，停止計算。
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 > stone2:
                heapq.heappush(stones, stone2 - stone1)

        # 若還有石頭剩下，回傳最後一塊石頭的重量，否則回傳0。
        return -heapq.heappop(stones) if len(stones) else 0


"""
這個程式碼的時間複雜度是 O(nlogn)，其中 n 是石頭的數量。
這是由於建立heap的時間複雜度是O(n)，然後在while循環中，
每次取出最大的兩塊石頭並將一個新的石頭放回heap中，
需要O(logn)時間，因此總時間複雜度是O(nlogn)。

空間複雜度是 O(n)，這是由於程式碼使用了一個列表來存儲石頭的重量，其大小是 n。 此外，程式碼使用了heap來存儲石頭，其大小也是 n。 因此，空間複雜度是O(n)。
"""


# @lc code=end
