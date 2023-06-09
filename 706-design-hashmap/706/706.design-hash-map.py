#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:
    def __init__(self):
        # 初始化一個包含1000001個元素的空列表，每個元素代表一個鍵值
        self.data = [None] * 1000001

    def put(self, key: int, val: int) -> None:
        # 將值放入對應的鍵中
        self.data[key] = val

    def get(self, key: int) -> int:
        # 從對應的鍵中取得值
        val = self.data[key]
        # 如果值存在，則返回它；否則返回 -1
        return val if val is not None else -1

    def remove(self, key: int) -> None:
        # 將對應的鍵中的值設為 None
        self.data[key] = None


# 時間複雜度分析：
# 假設散列表的大小是 n，那麼 put、get 和 remove 方法的時間複雜度均為 O(1)，因為它們只需要進行一次常數時間的查找或設置操作即可。

# 空間複雜度分析：
# 散列表的大小為 n，因此空間複雜度為 O(n)。在本題中，n 的值是固定的，為 1000001。因此，這個散列表的空間占用量是可以接受的。

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
