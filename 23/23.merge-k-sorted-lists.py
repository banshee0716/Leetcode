#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        n, interval = len(lists), 1

        while interval <= n:
            for start in range(0, n, interval * 2):
                if start + interval < n:
                    lists[start] = mergeTwoLists(lists[start], lists[start + interval])
            interval *= 2

        return lists[0]


# @lc code=end
