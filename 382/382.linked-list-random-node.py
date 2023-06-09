#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
        ans = 0
        p, i = self.head, 0
        while p:
            if random.randint(0, i) == 0:
                ans = p.val  # replace ans with i-th node.val with probability 1/i
            p = p.next
            i += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
