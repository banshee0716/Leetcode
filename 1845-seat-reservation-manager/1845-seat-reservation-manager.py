import heapq

class SeatManager:
    def __init__(self, n: int):
        # 初始化座位管理器，所有座位號碼初始化為未預約
        self.last = 0
        self.pq = []  # 創建一個最小堆

    def reserve(self) -> int:
        # 預約座位
        if not self.pq:
            # 如果沒有釋放的座位，分配新的座位號碼
            self.last += 1
            return self.last
        else:
            # 如果有釋放的座位，從最小堆中取出最小的號碼
            return heapq.heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        # 釋放座位
        if seatNumber == self.last:
            # 如果釋放的是最後一個分配的座位，減少last的值
            self.last -= 1
        else:
            # 否則，將釋放的座位號碼加入最小堆中
            heapq.heappush(self.pq, seatNumber)

"""
這題的解題思路可以用最小堆(min heap)來實現，因為最小堆能夠保證每次取出的都是最小元素。以下是步驟：

1. 初始化：建立一個最小堆來存儲釋放的座位號碼，並有一個last變量來記錄目前分配到的最後一個座位號碼。

2. 預約座位 (reserve)：
    -如果最小堆是空的，表示沒有釋放的座位，我們應該分配一個新座位，last變量加一，並返回該座位號碼。
    -如果最小堆不是空的，從最小堆中取出一個號碼並返回，這代表重新分配一個之前釋放的座位。

3. 釋放座位 (unreserve)：
    -如果釋放的座位號碼等於last，表示釋放的是最後一個分配的座位，將last減一。
    - 否則，將釋放的座位號碼放入最小堆中。
    
時間複雜度分析：
reserve：在最壞的情況下，當最小堆非空，這會花費 O(log n) 的時間來從堆中取出最小元素。
unreserve：在最壞的情況下，將一個元素加入最小堆中也是 O(log n) 的時間複雜度。

空間複雜度分析：
這個系統使用了一個最小堆來存儲釋放的座位，最壞情況下可能需要存儲所有n個座位的信息，所以空間複雜度為 O(n)。
"""



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)