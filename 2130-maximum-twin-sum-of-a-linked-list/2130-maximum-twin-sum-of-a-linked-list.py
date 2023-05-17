# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 初始化指針
        slow_ptr = head
        fast_ptr = head
        prev_ptr = None
        
        # 遍歷鏈表，反轉前半部分
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            next_node = slow_ptr.next
            slow_ptr.next = prev_ptr
            prev_ptr = slow_ptr
            slow_ptr = next_node
        
        # 初始化最大和
        max_sum = float('-inf')
        
        # 遍歷 slow_ptr 和 prev_ptr，計算最大和
        while slow_ptr:
            max_sum = max(max_sum, slow_ptr.val + prev_ptr.val)
            slow_ptr = slow_ptr.next
            prev_ptr = prev_ptr.next
        
        # 返回最大和
        return max_sum

    
'''
時間複雜度為 O(n)，其中 n 是鏈表的節點數量。我們需要遍歷鏈表兩次，一次是反轉前半部分，一次是計算最大和。空間複雜度為 O(1)，因為我們只使用了有限的指針和變量來處理鏈表。
'''