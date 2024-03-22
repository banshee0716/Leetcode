# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversed(self, head: ListNode):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next  # 保存当前节点的下一个节点
            cur.next = prev  # 翻转当前节点的指向
            prev = cur  # 将当前节点设置为下一次迭代的前一个节点
            cur = next_temp  # 移动到原始的下一个节点
            
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        rev = self.reversed(slow)
        while rev:
            if head.val != rev.val:
                return False
            else:
                head = head.next
                rev = rev.next
        
        return True