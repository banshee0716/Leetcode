
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 內部函數，目的是處理當前節點的child鏈表
        def unpack(head):
            cur = tail = head
            
            # 遍歷當前鏈表
            while cur:
                # 如果當前節點有child
                if cur.child:
                    # 遞歸調用unpack函數處理child鏈表
                    start, end = unpack(cur.child)
                    # 連接child鏈表的尾節點和當前節點的next節點
                    if cur.next: cur.next.prev = end
                    # 更新當前節點的next節點為child鏈表的頭節點
                    # 更新child鏈表頭節點的prev節點為當前節點
                    # 更新child鏈表尾節點的next節點為當前節點原本的next節點
                    # 清空當前節點的child指針
                    cur.next, start.prev, end.next, cur.child = start, cur, cur.next, None
                    # 跳到child鏈表的尾部，繼續處理下一個節點
                    cur = end
                # 更新tail為當前節點
                tail = cur
                # 處理下一個節點
                cur = cur.next
            
            # 返回已處理鏈表的頭和尾
            return (head, tail)

        # 調用unpack函數並返回結果的頭節點
        return unpack(head)[0]

"""
時間複雜度: O(N)，其中 N 是所有節點的數量。雖然我們有遞歸調用，但每個節點只被處理一次。

空間複雜度: O(M)，其中 M 是多層鏈表中的最大層數。這是遞歸所需的最大調用堆棧大小。