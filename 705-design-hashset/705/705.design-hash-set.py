#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:
    def __init__(self):
        # 初始大小為 10000 的桶，每個桶存儲元素的列表。
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        # 獲取 key 的 hash 值和對應的桶。
        bucket, idx = self._index(key)
        if idx >= 0:
            # 如果已經存在 key 則不執行任何操作。
            return
        bucket.append(key)

    def remove(self, key):
        # 獲取 key 的 hash 值和對應的桶。
        bucket, idx = self._index(key)
        if idx < 0:
            # 如果不存在 key 則不執行任何操作。
            return
        bucket.remove(key)

    def contains(self, key):
        # 獲取 key 的 hash 值和對應的桶。
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        # 簡單地計算 key 的餘數作為 hash 值。
        return key % self.size

    def _index(self, key):
        # 獲取 key 的 hash 值和對應的桶。
        hash = self._hash(key)
        bucket = self.buckets[hash]
        # 查找桶中是否已經存在 key。
        for i, k in enumerate(bucket):
            if k == key:
                # 如果找到 key 則返回對應的桶和索引。
                return bucket, i
        # 如果沒有找到 key 則返回對應的桶和 -1。
        return bucket, -1


"""
時間複雜度：add, remove, contains 方法的時間複雜度為 O(1)，因為它們僅涉及單個桶中的操作。

空間複雜度：初始化時需要創建大小為 10000 的桶，因此空間複雜度為 O(1)。
"""


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
