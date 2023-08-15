# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 創建兩個臨時頭結點，before和after
        # before鏈表用來存放小於x的節點，after鏈表用來存放大於或等於x的節點
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after
        
        # 遍歷原始鏈表
        while head:
            if head.val < x:
                # 將節點加入到before鏈表中
                before_curr.next, before_curr = head, head
            else:
                # 將節點加入到after鏈表中
                after_curr.next, after_curr = head, head
            
            head = head.next
            
        # 將after鏈表的尾部設為None
        after_curr.next = None
        # 連接before和after兩個鏈表
        before_curr.next = after.next
        
        return before.next

        
    """
給定鍊錶的頭和值 x，對其進行分區，使得所有小於 x 的節點都位於大於或等於 x 的節點之前。

您應該保留兩個分區中節點的原始相對順序。

解題思路
開兩個鍊表節點分別是大於或是小於x，最後再接起來

時間複雜度：O(n)，其中n是給定鏈表的長度，因為我們只遍歷了鏈表一次。
空間複雜度：O(1)，我們只使用了固定的額外空間來存儲臨時鏈表的頭結點和當前節點。
    """