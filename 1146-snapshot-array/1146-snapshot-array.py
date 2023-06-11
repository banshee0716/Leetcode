class SnapshotArray:
    def __init__(self, length: int):
        # 初始化一個字典來存儲每個索引的值的歷史記錄
        self.map = defaultdict(list)
        # 初始化快照id
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        # 如果當前索引已經有值且其最新的快照id與當前的快照id相同，則直接更新該值
        if self.map[index] and self.map[index][-1][0] == self.snapId:
            self.map[index][-1][1] = val
            return
        # 如果當前索引沒有值，或者其最新的快照id與當前的快照id不同，則追加一個新的歷史記錄
        self.map[index].append([self.snapId, val])

    def snap(self) -> int:
        # 創建一個新的快照，並增加快照id
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        # 從字典中獲取索引的歷史記錄
        arr = self.map[index]
        # 二分查找到第一個快照id大於目標快照id的歷史記錄
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        # 如果不存在快照id小於或等於目標快照id的歷史記錄，則返回0
        if ans == -1: return 0
        # 否則，返回最新的歷史記錄的值
        return arr[ans][1]
    
"""
解題思路:

使用字典來儲存每個索引的值的歷史記錄，並與快照id一起儲存。當設置值時，檢查當前索引的最新快照id是否與當前快照id相同。如果相同，則更新該值；否則，追加一個新的歷史記錄。當創建快照時，增加快照id。當查詢值時，使用二分查找找到第一個快照id大於目標快照id的歷史記錄，並返回其前一個歷史記錄的值。

時間複雜度:

set操作的時間複雜度為O(1)。
snap操作的時間複雜度為O(1)。
get操作的時間複雜度為O(logN)，其中N為索引的歷史記錄數量。
空間複雜度:

O(M)，其中M為set操作的次數。每次set操作可能會將一個新的歷史記錄添加到字典中。
"""

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)