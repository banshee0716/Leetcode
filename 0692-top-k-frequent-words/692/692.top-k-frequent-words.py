#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start

# 引入 heapq 模塊以使用優先隊列功能
from heapq import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 初始化一個字典存儲每個單詞出現的次數
        ump = {}
        # 初始化一個列表存儲結果
        res = []

        # 遍歷 words 中的每個單詞，計算其出現次數
        for i in words:
            ump[i] = ump.get(i, 0) + 1

        # 初始化一個最大堆
        maxheap = []

        # 遍歷字典中的單詞和對應的出現次數
        for key, val in ump.items():
            # 將出現次數的負數和單詞一起放入最大堆中
            # 這樣做是因為 heapq 模塊僅支持最小堆，我們需要最大堆來按出現次數排序
            heappush(maxheap, [-val, key])

        # 從最大堆中彈出 k 個元素，並將單詞添加到 res 列表中
        for _ in range(k):
            val, key = heappop(maxheap)
            res.append(key)

        # 返回結果列表
        return res


"""
時間複雜度分析：

遍歷 words 列表的時間複雜度為 O(n)，其中 n 為 words 的長度。
將 n 個單詞和對應的出現次數加入最大堆的時間複雜度為 O(nlogn)。
從最大堆中彈出 k 個元素的時間複雜度為 O(klogn)。
綜合以上分析，此算法的總時間複雜度為 O(n + nlogn + klogn) = O(nlogn + klogn)。

空間複雜度分析：

字典 ump 的空間複雜度為 O(n)，其中 n 為不同單詞的數量。
最大堆 maxheap 的空間複雜度為 O(n)。
結果列表 res 的空間複雜度為 O(k)。
綜合以上分析，此算法的總空間複雜度為 O(n + n + k

"""
# @lc code=end
