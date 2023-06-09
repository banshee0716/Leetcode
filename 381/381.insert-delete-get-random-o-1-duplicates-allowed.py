#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
from sortedcontainers import SortedList
import random
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        # SortedList 用於保持元素的有序性，並且支援二分搜索
        self.arr = SortedList([])
        # defaultdict 用於存儲每個元素的數量
        self.dc = defaultdict(lambda: 0)

    def insert(self, val: int) -> bool:
        # 將元素插入到 SortedList 中，並更新 defaultdict 的值
        self.arr.add(val)
        self.dc[val] += 1
        # 如果插入的元素之前不存在，則返回 True
        return self.dc[val] == 1

    def remove(self, val: int) -> bool:
        # 如果元素存在，則移除並返回 True，否則返回 False
        if self.dc[val] > 0:
            self.arr.discard(val)
            self.dc[val] -= 1
            return True
        return False

    def getRandom(self) -> int:
        # 從 SortedList 中隨機選擇一個元素並返回
        return random.choice(self.arr)


"""
時間複雜度和空間複雜度：

時間複雜度：插入操作的時間複雜度為 O(log n)，移除操作的時間複雜度為 O(log n)，獲取隨機元素的時間複雜度為 O(1)。

空間複雜度：O(n)，其中 n 為元素的數量。因為我們需要存儲所有的元素和它們的數量。
"""


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
