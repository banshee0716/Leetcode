"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        # 若頭節點為空，直接返回
        if not head:
            return head

        # 創建一個虛擬節點
        dummy = Node(0)
        curr, stack = dummy, [head]

        # 開始DFS遍歷
        while stack:
            # 取出最後一個節點
            last = stack.pop()

            # 若有next節點，先放入stack
            if last.next:
                stack.append(last.next)

            # 若有child節點，後放入stack
            if last.child:
                stack.append(last.child)

            # 更新當前節點的next指標並清空child指標
            curr.next = last
            last.prev = curr
            last.child = None
            curr = last

        # 移除dummy節點並返回
        res = dummy.next
        res.prev = None
        return res


"""

解題思路是使用一個棧（Stack）來輔助遍歷。這種遍歷方式叫做深度優先遍歷（DFS）。
對於每個節點，我們首先檢查其next節點是否存在，如果存在就將其壓入棧；然後我們檢查其child節點是否存在，如果存在也壓入棧。這種順序保證了child鏈表先被處理。

時間複雜度: O(N)，其中 N 是所有節點的總數。因為我們確保每個節點都只被處理一次。

空間複雜度: O(M)，其中 M 是多層鏈表中的最大層數。這是因為我們使用了一個棧來保存每一層的節點。在最差情況下，我們可能需要存放所有的節點到棧中。
"""
