# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 將兩個鏈表轉換為數字
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        # 將兩個數字相加並轉換為字符串
        ans = str(num1 + num2)

        # 創建一個新的鏈表來存儲結果
        dummylist = dummy = ListNode(0)
        for i in ans:
            dummy.next = ListNode(int(i))
            dummy = dummy.next
            
        return dummylist.next

"""
時間複雜度是O(N + M)，其中N和M分別是兩個鏈表的長度。我們需要遍歷兩個鏈表來將它們轉換為數字，並遍歷結果的每一個字符來創建結果鏈表。

空間複雜度是O(max(N, M))，這是因為我們創建了一個新的鏈表來存儲結果，其長度與兩個輸入鏈表的較長者相等。
"""