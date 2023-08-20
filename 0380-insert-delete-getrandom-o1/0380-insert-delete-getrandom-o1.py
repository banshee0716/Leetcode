class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.arr.append(val)
        self.indices[val] = len(self.arr)-1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        i = self.indices[val]
        
        # Update the index of arr[-1] in the indices.
        self.indices[self.arr[-1]] = i
        
        # Move the last element to the i th position.
        self.arr[i] = self.arr[-1]
        
        # remove the last element, and remove the index of val
        self.indices.pop(val)
        self.arr.pop()
        
        return True
        

    def getRandom(self) -> int:
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
"""