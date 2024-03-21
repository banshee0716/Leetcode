# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next_node = cur.next  # 暫存cur的下一個節點
            cur.next = prev  # 反轉指針
            prev = cur  # 更新prev為當前節點
            cur = next_node  # 移動到下一個節點
        
        return prev

    """
1. 初始化：創建兩個指針prev和cur。prev初始化為None，cur初始化為鏈表的頭節點head。

2. 迭代遍歷鏈表：當cur不為None時，持續迭代。在每次迭代中，執行以下操作：
    -暫存cur的下一個節點next_node。
    -將cur.next指向prev，實現反轉。
    -更新prev和cur，為下一次迭代準備。
    
3. 返回新的頭節點：當迭代完成（即cur為None），prev將會是反轉後的鏈表的新頭節點。

時間複雜度
    -此算法的時間複雜度為O(n)，其中n是鏈表的節點數量。這是因為我們需要遍歷鏈表一次來反轉每個節點的指向。

空間複雜度
    -此算法的空間複雜度為O(1)。我們只使用了固定的額外空間（prev, cur, 和next_node指針）。
    """