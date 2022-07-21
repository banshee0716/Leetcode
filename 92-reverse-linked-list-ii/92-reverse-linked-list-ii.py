class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        
        cur, prev = head, dummy
        for _ in xrange(m - 1):
            cur = cur.next
            prev = prev.next
        
        for _ in xrange(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next