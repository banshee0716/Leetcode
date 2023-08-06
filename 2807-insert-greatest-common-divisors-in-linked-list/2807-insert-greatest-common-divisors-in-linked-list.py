# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            node.next = ListNode(gcd(node.val, node.next.val), node.next)
            node = node.next.next
            
        return head
        
        
"""    
給定鍊錶頭的頭，其中每個節點都包含一個整數值。

在每對相鄰節點之間，插入一個新節點，其值等於它們的最大公約數。

返回插入後的鍊錶。

兩個數的最大公約數是能整除兩個數的最大正整數。
"""