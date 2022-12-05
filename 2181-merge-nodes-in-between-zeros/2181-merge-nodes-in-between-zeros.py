# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        s = 0
        while head:
            if head.val:
                s += head.val
            else:
                if s:
                    cur.next = ListNode(s)
                    cur = cur.next
                    s = 0
            head = head.next
            
        return dummy.next
