class OrderedStream:

    def __init__(self, n: int):
        # 初始化一個長度為n的串列，用於存儲數據流中的元素
        self.stream = [None] * n
        # 初始化指針ptr為0，表示目前可以插入的位置
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        # 由於題目給的idKey是從1開始的，所以要減1轉成0開始的索引
        idKey -= 1
        # 將值插入到指定位置
        self.stream[idKey] = value
        
        # 如果當前指針位置在插入的索引之前，則直接返回空串列
        if self.ptr < idKey:
            return []
        
        else:
            # 如果當前指針位置與插入的索引位置相同或之前，則尋找下一個為None的位置
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            # 返回從插入索引到當前指針位置的子串列
            return self.stream[idKey:self.ptr]
"""
解題思路：

1. 初始化一個長度為n的串列和一個指針ptr。
2. 當插入一個元素時，先檢查指針位置是否在插入的索引之前。
3. 如果是，直接返回空串列。
4. 如果否，更新指針位置到下一個為None的位置，並返回從插入索引到當前指針位置的子串列。

時間複雜度：

__init__方法的時間複雜度是O(n)，其中n是數據流的長度。
insert方法的平均時間複雜度是O(1)，但在最壞情況下可能需要O(n)，這是因為可能需要尋找整個數據流中的下一個為None的位置。
空間複雜度：O(n)，其中n是數據流的長度。
"""
        
"""
有一個 n (idKey, value) 對以任意順序到達的流，其中 idKey 是 1 到 n 之間的整數，value 是字符串。沒有兩對具有相同的 id。

設計一個流，通過在每次插入後返回一個值塊（列表），按 ID 的升序返回值。所有塊的串聯應該產生一個排序值的列表。
"""

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)