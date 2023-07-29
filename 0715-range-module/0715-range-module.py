import bisect


class RangeModule:
    def __init__(self):
        # 初始化範圍集合
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        # 尋找左右邊界應該插入的位置
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            # 如果start是偶數，則左邊界不在任何區間內，需要添加
            subtrack.append(left)
        if end % 2 == 0:
            # 如果end是偶數，則右邊界不在任何區間內，需要添加
            subtrack.append(right)

        # 更新範圍集合
        self.track[start:end] = subtrack

    def removeRange(self, left: int, right: int) -> None:
        # 尋找左右邊界應該插入的位置
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            # 如果start是奇數，則左邊界在某個區間內，需要添加
            subtrack.append(left)
        if end % 2 == 1:
            # 如果end是奇數，則右邊界在某個區間內，需要添加
            subtrack.append(right)

        # 更新範圍集合
        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        # 尋找左右邊界在track中的位置
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        # 如果start和end相同並且為奇數，則[left, right)在範圍內
        return start == end and start % 2 == 1


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

"""
甚至可以直接説(一個解答區主流的)做法就是用一個能按key排序的容器
(以C++而言就是map<int,int>)，key是左端，value是右端
去維護區間的起點(閉)和終點(開)
"""

"""
這裡使用了一種稱為"閉開區間"的表示方式，將每一個範圍表示為兩個數字，閉區間的左端點和開區間的右端點。

我們可以使用一個list track 來維護所有範圍，並保持 track 中的元素按照升序排列。
因此，當我們需要添加或刪除一個範圍時，我們可以使用二分查找來找到對應的插入點，然後更新 track。

時間複雜度為O(logn)，其中n是當前track中的區間數。因為我們使用了二分查找，所以每次查找、添加和刪除操作都是O(logn)。
至於空間複雜度，取決於track中的區間數，最壞的情況是O(n)，即每次添加的區間都不與現有的區間重疊。
"""