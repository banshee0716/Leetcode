import random

class RandomizedSet:
    def __init__(self):
        # 存儲元素的陣列
        self.arr = []
        # 存儲元素索引的字典
        self.indices = {}
        
    def insert(self, val: int) -> bool:
        # 若元素已存在，返回 False
        if val in self.indices:
            return False
        # 將元素加入到陣列末尾，並保存其索引
        self.arr.append(val)
        self.indices[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        # 若元素不存在，返回 False
        if val not in self.indices:
            return False
        
        i = self.indices[val]
        
        # 更新最後一個元素在 indices 中的索引值
        self.indices[self.arr[-1]] = i
        
        # 將最後一個元素移到 i 這個位置
        self.arr[i] = self.arr[-1]
        
        # 移除最後一個元素並從字典中刪除 val 的索引
        self.indices.pop(val)
        self.arr.pop()
        
        return True
        
    def getRandom(self) -> int:
        # 隨機選擇一個元素並返回
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
實現 RandomizedSet 類：

RandomizedSet() 初始化 RandomizedSet 對象。
bool insert(int val) 如果項目 val 不存在，則將其插入集合中。如果該項不存在則返回 true，否則返回 false。
bool remove(int val) 從集合中刪除項目 val（如果存在）。如果該項目存在則返回 true，否則返回 false。
int getRandom() 從當前元素集中返回一個隨機元素（調用此方法時保證至少存在一個元素）。每個元素必須具有相同的返回概率。
您必須實現類的函數，以便每個函數的平均時間複雜度為 O(1)。

insert: O(1)
remove: O(1)
getRandom: O(1)
"""