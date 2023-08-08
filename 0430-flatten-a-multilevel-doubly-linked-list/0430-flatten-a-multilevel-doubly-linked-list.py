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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0)
        curr, stack = dummy, [head]
        while stack:
            last = stack.pop()
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
                
            curr.next = last
            last.prev = curr
            last.child = None
            curr = last
            
        res = dummy.next
        res.prev = None
        return res