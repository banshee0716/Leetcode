# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # 初始化一個虛擬節點(dummy node)，並將其下一個節點指向連結串列的頭節點
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # 當前處理的節點設為虛擬節點
        current_node = dummy_head
        
        # 遍歷連結串列
        while current_node.next != None:
            # 如果當前節點的值等於val
            if current_node.next.val == val:
                # 刪除該節點，即將前一個節點的next指向當前節點的next
                current_node.next = current_node.next.next
            else:
                # 如果當前節點的值不等於val，則移動到下一個節點
                current_node = current_node.next
                
        # 返回虛擬節點的下一個節點，即為修改過後的連結串列的頭節點
        return dummy_head.next
    
    
"""
對於時間複雜度，由於我們遍歷了所有的節點，因此時間複雜度為O(n)，其中n是連結串列的長度。
對於空間複雜度，由於我們只用到了一個額外的節點(dummy node)，因此空間複雜度為O(1)。
"""